---
created: '2024-02-19 01:18:10'
date: 2008-01-06 00:00:00+00:00
description: ''
fname: pub.post.2008.01.pagetemplate-for-site-generation
id: 0ez6ookvm4l8vgwg2i9j3ck
redirects:
- /blogspot/2008/01/06_pagetemplate-for-site-generation.html
- /post/2008/pagetemplate-for-site-generation/
- /2008/01/06/pagetemplate-for-site-generation/
slug: pagetemplate-for-site-generation
tags:
- pagetemplate
- ruby
- blogspot
title: Pagetemplate for Site Generation
updated: '2024-08-07 18:33:35'
---

So I was looking at the Python Blogger client from [Python Loves Blogger (Part 1)]({{< relref "/post/2007/12/python-loves-blogger-part-1.md" >}}), and I tried implementing the same thing in [Ruby]({{< relref "/card/ruby/_index.md" >}}). [gdata-ruby](https://code.google.com/p/gdata-ruby-util/) confusion stymied me. I still don't know whether library issues or my own ignorance blocked me.
<!--more-->

That, of course, set me off on yet another thought. What if I tried to define my posts in a [Pagetemplate]({{< relref "/post/2002/06/pagetemplate.md" >}}) file and used filters to handle the dirty work? Well, that might be a little challenge. But what if I used this approach to generate a whole Web site? Okay, yeah. That may have come out of nowhere for you. The truth is that I love static site generation tools, from [ZenWeb](http://zenspider.com/ZSS/Products/ZenWeb/index.html) to [WebMake](http://webmake.taint.org). These tools appeal to me because [Coolnamehere]({{< relref "/card/coolnamehere.md" >}}) is a static site and I love anything which can give that pile of pages a common format without making heavy server demands. Honestly, loading up PHP just so I can have a templated site seems like overkill.

Let's see if I can build a site like coolnamehere with Ruby and PageTemplate. I plan to borrow heavily from ZenWeb, since there are a lot of things to like about the ZenSpider approach. I especially like   building a site from a collection of pages and a chain of filters. Hey, PageTemplate has filters thanks to Greg Millam. Why don't I try *using* them?

## Start Small

I am going to start small, by teaching SiteTemplate about [Maruku](https://github.com/bhollis/maruku).

It took me a bit of time to get that much done, because I needed to relearn how PageTemplate initializes. *Note to self: don't ever go a full year without using your own library.*

The test is simple: create a template using the Maruku filter. Compare the output of that template with the text minus PageTemplate directives and fed into Maruku. The test passes if they look alike, or close enough.

``` ruby
#!/usr/local/bin/ruby

require 'rubygems'
require 'test/unit'
require 'sitetemplate'

class TC_MarukuFilter < Test::Unit::TestCase
  require 'maruku'

  def test_maruku_filter
    content = "This is a paragraph"

    # template_file contains the text "[%filter :maruku%]This is a paragraph[%end%]"
    template_file = "maruku.txt"
    maruku_doc = Maruku.new(content)
    pt = PageTemplate.new()
    pt.load(template_file)
    assert_equal(maruku_doc.to_html + "\n", pt.output,
      "Check if Maruku filter ran successfully")
  end
end
```

Then the code I needed to make that test pass:

``` ruby
#!/usr/local/bin/ruby
# Utility for generating a static site with PageTemplate

require 'rubygems'
require 'maruku'
require 'pagetemplate'

class PageTemplate
  class DefaultPreprocessor
    class << self
      def maruku(text)
        return Maruku.new(text).to_html
      end
    end
  end
end
```

I cut corners by adding the `maruku` filter method to PageTemplate's DefaultPreprocessor. PageTemplate's internals need a little work, since this isn't the prettiest way a person might want to add filters. It works well, but it's not pretty.

That works well enough. Next time I'll try a template filter, which puts the Maruku output into a template file of my choosing. That way we get the standard look for pages.