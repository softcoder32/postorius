# -*- coding: utf-8 -*-
# Copyright (C) 1998-2010 by the Free Software Foundation, Inc.
#
# This file is part of GNU Mailman.
#
# GNU Mailman is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# GNU Mailman is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# GNU Mailman.  If not, see <http://www.gnu.org/licenses/>.

import mailmanweb

from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Import mailman urls and set urlpatterns if you want to hook
# mailman_django into an existing django site. 
# Otherwise set ROOT_URLCONF in settings.py to
# `mailman_django.urls`.
# from mailman_django import urls as mailman_urls

urlpatterns = patterns('',
    url(r'^$', 'mailmanweb.views.list_index'),
    (r'^mailmanweb/', include('mailmanweb.urls')),
	url(r'', include('social_auth.urls')),
)
