# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PerlExtutilsMakemaker(PerlPackage):
    """ExtUtils::MakeMaker - Create a module Makefile. This utility is designed
    to write a Makefile for an extension module from a Makefile.PL. It is based
    on the Makefile.SH model provided by Andy Dougherty and the perl5-porters.
    """
    homepage = "https://github.com/Perl-Toolchain-Gang/ExtUtils-MakeMaker"
    url      = "http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/ExtUtils-MakeMaker-7.24.tar.gz"

    version('7.24', '15c67ba2ea2c9e20a3d976b738adb113')

    depends_on('perl@5.6.0:', type=('build', 'run'))
