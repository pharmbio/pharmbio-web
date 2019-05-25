+++
title = "SciPipe workflow tool published in GigaScience and CiSe"
description = "TBC"
date = "2019-05-25T01:14:00+01:00"
taxonomies = "blogging"
teaser_image = "/img/scipipe-gigascience.png"
+++

<a href="https://pharmb.io/publication/2019-scipipe/" target="_blank"><img src="/img/scipipe-gigascience.png" style="float: right; width: 37%; margin: 0 0 1em 2em; clear: both; box-shadow: 2px 2px 12px rgb(0,0,0,0.25);"/></a>

A few weeks ago the workflow tool we have developed and used in the group,
[SciPipe](https://pharmb.io/tool/scipipe/), [was published in Gigascience](https://pharmb.io/publication/2019-scipipe/).
This article quite comprehensively summarizes our lessons learned in scientific
workflow usage and design over the last couple of years, reviewing a dozen other tools,
and carefully motivates and explains the design of this new workflow library.
An accompanying popular science views article was also just
[published in the IEEE magazine "Computers in Science and Engineering"](https://doi.org/10.1109/MCSE.2019.2907814), providing some
further info on our views on SciPipe and its direction.

A fun sidenote is that we notice the SciPipe publication has been at the top of
the "most read" GigaScience GigaScience publications, over the last three weeks
(See the "most read" tab on [this page](https://academic.oup.com/gigascience/pages/in_the_news))
In the same go, [SciPipe repository](https://github.com/scipipe/scipipe/) also
passed 500 stars on GitHub, reflecting a significant interest in the library
from the community.

Anyways, these two publications come after the publication of the [first scientific study performed with SciPipe, last year, on building predictive target profiles](https://pharmb.io/publication/2018-ptp/) and mark an important
milestone in the SciPipe project. It thus seems like a good time to provide a
small recap of the project's focus and a look into the future.

## A focus on simplicity, supporting complexity

<a href="https://academic.oup.com/gigascience/pages/in_the_news" target="_blank"><img src="/img/scipipe-most-read.png" style="float: right; width: 37%; margin: 1em 0 1em 2em; clear: both; box-shadow: 2px 2px 12px rgb(0,0,0,0.25);"/></a>

SciPipe has taken a rather different direction than many other contemporary
workflow tools and libraries. Rather than building a lot of new technology,
we have strived hard to boil down the library to the bare necessary parts
to do what it really ought to do: Schedule and keep track of compute tasks
and safely manage their corresponding input and output data, in a way as
generic as possible. This strive for essential simplicity and genericity
in the end is in our experience what is required thought to support what
SciPipe shines for: Really complex workflows. In other words, to support
really complex workflow usecases, we have needed to strive for a really
simple and generic workflow scheduling library.

## Maintainabiltiy for the long term

The focus can be seen in such characteristics as zero outside dependencies,
apart from the ubiquitious bash shell and a Unix/Linux-like operating system
(Windows is well supported via Cygwin / MSYS2). The code base is also kept
extremely small, not much more than 1000-1500 lines of code. One of the
motivation factors for this, is to keep SciPipe maintaineable in the future,
even without a large team of developers. Another consequence is that SciPipe
can most suitably be included into the source code of users' own workflow code
repositories (as known as "vendoring" in the Go world), to ensure the
functioning and maintenance of workflows for the long run.

## What this means for the future

This focus also gives some hints on where SciPipe is headed for the future.  We
don't see us trying to add every possible bell-and-whistle into the core of
SciPipe, but will rather spend time on further streamlining its core function
and making its programming API easier to use. We might add more convenience
functionality still though, but then we tend to add that to the separate
scipipe helper tool, which is itself not at all required for workflows to work
(thus not needed to be included in workflow repos).

Welcome to try SciPipe out, for your next project! (Find us in the [SciPipe Gitter chat](https://gitter.im/scipipe/scipipe)
for community backed support,
and any questions!).

## Links

- [Main website and documentation](https://scipipe.org)
- [GitHub repository](https://github.com/scipipe/scipipe)
- [Publication in GigaScience](https://pharmb.io/publication/2019-scipipe/)
- [Publication in IEEE / CiSE](https://doi.org/10.1109/MCSE.2019.2907814)
