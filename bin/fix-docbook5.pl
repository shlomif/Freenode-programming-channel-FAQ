#! /usr/bin/env perl
#
# Short description for fix-docbook5.pl
#

use strict;
use warnings;
use 5.014;
use autodie;

use Carp                                   qw/ confess /;
use Getopt::Long                           qw/ GetOptions /;
use Path::Tiny                             qw/ cwd path tempdir tempfile /;
use Docker::CLI::Wrapper::Container v0.0.4 ();

sub run
{
    my $fh      = path("first-version-of-docbook5-FAQ.docbook5.xml");
    my $content = $fh->slurp_utf8();
    $content =~
s#<(/?)a\b((?:\s+href)?)#"<" . $1 . "link" . ($2 ? " xlink:href" : "")#egms;
    $content =~ s#<(/?)q\b#"<" . $1 . "quote"#egms;
    $fh->spew_utf8($content);
    return;
    my $output_fn;

    GetOptions( "output|o=s" => \$output_fn, )
        or die "errror in cmdline args: $!";

    if ( !defined($output_fn) )
    {
        die "Output filename not specified! Use the -o|--output flag!";
    }

    exit(0);
}

run();

1;

__END__

=encoding UTF-8

=head1 NAME

=head1 COPYRIGHT AND LICENSE

This software is Copyright (c) 2007 by Shlomi Fish.

This is free software, licensed under:

  The MIT (X11) License

=cut
