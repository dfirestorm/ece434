temp = `i2cget -y 2 0x48 0`
temp2 = $($temp * 5)
echo $temp2