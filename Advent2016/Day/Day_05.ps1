$md5 = New-Object -TypeName System.Security.Cryptography.MD5CryptoServiceProvider
$utf8 = New-Object -TypeName System.Text.UTF8Encoding
$str = "ugkcyxxp"
$done = $false
$idx = 0
$i = 0
$a = @( '-','-','-','-','-','-','-','-')
$remaining = 8;
while ($done -eq $false) {
	$hash = [System.BitConverter]::ToString($md5.ComputeHash($utf8.GetBytes("$str$i"))).Replace('-','')
	$s = $hash.Substring(0,5)
	if ($s -eq '00000') {
		Write-Host $hash
		$idx = $idx + 1
	}
	$aIdx = ([int]$hash[5]-48)
	
	if ($a[$aIdx] -eq '-') {
		try	{
			$a[$aIdx] = $hash[6]
		} catch {
		}
	}
	
	$i = $i + 1
	
	if ($idx -ge 8 -and (($a | ? { $_ -eq '-' }).Length -eq 0 )) {
		$done = $true
	}
}