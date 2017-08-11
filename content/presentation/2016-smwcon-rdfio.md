+++
draft = false
title = "Batch import of large RDF datasets using RDFIO or the new rdf2smw tool"
date = 2016-09-30T12:20:00+02:00
thumb_img = "/thumbs/pres-2016-smwcon-rdfio.png"
author = ["Samuel Lampa"]
abstract = "The RDFIO extension was developed for being able to import datasets consisting of plain RDF triples, for collaborative editing and further export, or just as a means to bootstrap a wiki structure based on an existing dataset. In our research at the Pharmaceutical Bioinformatics group at Uppsala University, we are simultaneously interested in semantic approaches, and the challenges of big data, as produced by new high throughput laboratory techniques in the life sciences. We have thus experimented with importing datasets of a somewhat larger size (so far up to ~0.5 million triples) into Semantic MediaWiki. This has put the RDFIO extension to the test, and hinted at the need to develop e.g. a commandline interface for the import function. To be able to quickly iterate on different settings for converting RDF to wiki page structures without needing to run a full import, we have also developed an alternative approach for RDF import, using a standalone tool, rdf2smw, that converts from RDF to SMW pages and facts in MediaWiki XML format, which means that the resulting wiki content can be manually verified (and settings changed), before the full, time-consuming import, which is then done via MediaWiki's main XML import function. Finally, to support the development and experimentation, we have also created an automated vagrant box installation of MW, SMW and RDFIO, which we will mention."
venue = "SMWCon Fall 2016"
venue_url = "https://www.semantic-mediawiki.org/wiki/SMWCon_Fall_2016/Batch_import_of_large_RDF_datasets_using_RDFIO_or_the_new_rdf2smw_tool"
city = "Frankfurt"
youtube_id = "k70er1u1ZYs"
vimeo_id = ""
slideshare_id = "66590899"
slides_doi = ""
+++
