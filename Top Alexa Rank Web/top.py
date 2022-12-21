import os

from ioweb import Crawler, Request


class TopCrawler(Crawler):
    limit_pages = 1300

    def task_generator(self):
        with open('data/top-1m.csv') as inp:
            for lnum, line in enumerate(inp):
                if (lnum + 1) == self.limit_pages:
                    break
                else:
                    _, hostname = line.strip().split(',', 1)
                    path = self.build_doc_location(hostname)
                    if os.path.exists(path):
                        self.stat.inc('skip-doc-exists')
                    else:
                        yield Request(
                            name='page',
                            url='http://%s' % hostname,
                            meta={
                                'hostname': hostname,
                            },
                        )

    def build_doc_location(self, hostname):
        return 'data/html/top1k/%s.html' % hostname

    def handler_page(self, req, res):
        if res.css('title'):
            self.stat.inc('page-ok')
            res.save(self.build_doc_location(req.meta['hostname']))
        else:
            self.stat.inc('page-fail-no-title')
