from pyquery import PyQuery as pq
url = 'http://fgowiki.com/'
doc = pq(url)
# addclass removeclass
a = doc('.col-md-3.navi li a')
print(a)
a.remove_class('gamevbg')
print(a)
a.add_class('gamevbg')
print(a)
print('___________________________________')
# atts css
a.attr('name','test')
print(a)
a.css('align','center')
print(a)
print('___________________________________')
# remove
html = """
<div class="wrap">
Hello World
<p>sadasdasdasdasdasda</p>
</div>

"""
text = pq(html)
wrap = text('.wrap')
print(wrap.text())
wrap.find('p').remove()
print(wrap.text())

