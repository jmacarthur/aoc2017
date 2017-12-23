#!/usr/bin/perl -w

my $lineno = 0;

while(my $l = <>) {
    print("inst$lineno:\n");
    chomp($l);
    $c = $l;
    
    $c =~ s/set (.) (.*)/$1 = $2;/;
    if($c =~ /jnz (.*) (.*)/) {
	$dest = $lineno + $2;
	$c = "if($1 != 0) goto inst$dest;";
    }
    $c =~ s/mul (.*) (.*)/$1 *= $2;/;
    $c =~ s/sub (.*) (.*)/$1 -= $2;/;
    print "$c /* $l */\n";
    $lineno++;
}

print("inst$lineno:\n");
