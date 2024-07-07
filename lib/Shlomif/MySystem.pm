package Shlomif::MySystem;

use strict;
use warnings;

use parent 'Exporter';

our @EXPORT_OK = (qw/ my_system my_exec_perl /);

sub my_system
{
    my $cmd = shift;
    my $err = shift || '';

    # print join( ' ', @$cmd ), "\n";
    if ( system(@$cmd) )
    {
        die "<<@$cmd>> failed $err.";
    }
}

sub my_exec_perl
{
    my ( $cmd, $err ) = @_;

    return my_system( [ $^X, '-Ilib', @$cmd ], $err );
}

1;

__END__
