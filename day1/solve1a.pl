$t=0;$l=<>;chomp($l);@l=split //,$l;$a=$#l+1;for($i=0;$i<$a;){$t+=$l[$i]if($l[$i]eq$l[(++$i)%$a]);}print$t;
