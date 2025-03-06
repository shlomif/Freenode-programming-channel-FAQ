#!/usr/bin/env perl

use strict;
use warnings;
use autodie;
use lib './lib';
use Shlomif::MySystem qw/ my_system /;

my_system(
    [
        'cookiecutter', '-f', '--no-input',
        'gh:shlomif/cookiecutter--shlomif-latemp-sites',
        'project_slug=.',
    ],
    'cookiecutter failed.'
);
