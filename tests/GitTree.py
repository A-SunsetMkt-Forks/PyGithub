############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

from __future__ import annotations

from . import Framework


class GitTree(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.tree = self.g.get_user().get_repo("PyGithub").get_git_tree("f492784d8ca837779650d1fb406a1a3587a764ad")

    def testAttributes(self):
        self.assertEqual(self.tree.sha, "f492784d8ca837779650d1fb406a1a3587a764ad")
        self.assertEqual(len(self.tree.tree), 11)
        self.assertEqual(self.tree.tree[0].mode, "100644")
        self.assertEqual(self.tree.tree[0].path, ".gitignore")
        self.assertEqual(self.tree.tree[0].sha, "8a9af1462c3f4e3358315c2d2e6ef1e7334c59dd")
        self.assertEqual(self.tree.tree[0].size, 53)
        self.assertEqual(self.tree.tree[0].type, "blob")
        self.assertEqual(
            self.tree.tree[0].url,
            "https://api.github.com/repos/jacquev6/PyGithub/git/blobs/8a9af1462c3f4e3358315c2d2e6ef1e7334c59dd",
        )
        self.assertEqual(self.tree.tree[6].mode, "040000")
        self.assertEqual(self.tree.tree[6].path, "ReplayDataForIntegrationTest")
        self.assertEqual(self.tree.tree[6].sha, "60b4602b2c2070246c5df078fb7a5150b45815eb")
        self.assertEqual(self.tree.tree[6].size, None)
        self.assertEqual(self.tree.tree[6].type, "tree")
        self.assertEqual(
            self.tree.tree[6].url,
            "https://api.github.com/repos/jacquev6/PyGithub/git/trees/60b4602b2c2070246c5df078fb7a5150b45815eb",
        )
        self.assertIsNone(self.tree.truncated)
        self.assertEqual(
            self.tree.url,
            "https://api.github.com/repos/jacquev6/PyGithub/git/trees/f492784d8ca837779650d1fb406a1a3587a764ad",
        )

        self.assertEqual(
            repr(self.tree),
            'GitTree(sha="f492784d8ca837779650d1fb406a1a3587a764ad")',
        )
        self.assertEqual(
            repr(self.tree.tree[0]),
            'GitTreeElement(sha="8a9af1462c3f4e3358315c2d2e6ef1e7334c59dd", path=".gitignore")',
        )
