#! /usr/bin/env perl
#
# Short description for template-toolkit-render.pl
#
# Version 0.0.1
# Copyright (C) 2024 Shlomi Fish < https://www.shlomifish.org/ >
#
# Licensed under the terms of the MIT license.

use strict;
use warnings;
use 5.014;
use autodie;

use Carp         qw/ confess /;
use Getopt::Long qw/ GetOptions /;
use Path::Tiny   qw/ cwd path tempdir tempfile /;

sub run
{
    my $input_fn;
    my $output_fn;

    GetOptions(
        "input=s"  => \$input_fn,
        "output=s" => \$output_fn,
    ) or die "errror in cmdline args: $!";

    if ( !defined($input_fn) )
    {
        die "Input filename not specified! Use the --input flag!";
    }

    if ( !defined($output_fn) )
    {
        die "Output filename not specified! Use the --output flag!";
    }

    use Template;

    # some useful options (see below for full list)
    my $config = {
        INCLUDE_PATH => '/search/path',    # or list ref
        INTERPOLATE  => 1,                 # expand "$var" in plain text
        POST_CHOMP   => 1,                 # cleanup whitespace
        PRE_PROCESS  => 'header',          # prefix each template
        EVAL_PERL    => 1,                 # evaluate Perl code blocks
    };
    $config = +{};

    # create Template object
    my $template = Template->new($config);

    # define template variables for replacement
    my $vars = {};

    # specify input filename, or file handle, text reference, etc.
    # my $input = 'myfile.html';

    # process input template, substituting variables
    $template->process( $input_fn, $vars, $output_fn )
        || die $template->error();

    exit(0);
}

run();

1;

__END__

=encoding UTF-8

=head1 NAME

XML::Grammar::Screenplay::App::FromProto

=head1 VERSION

version v0.16.0

=head1 COPYRIGHT AND LICENSE

This software is Copyright (c) 2007 by Shlomi Fish.

This is free software, licensed under:

  The MIT (X11) License

=cut
