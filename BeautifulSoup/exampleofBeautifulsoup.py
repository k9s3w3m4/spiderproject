from bs4 import BeautifulSoup
html = """"
<li class="l-work-thumbnail">
<span class="work-thumbnail__badge work-thumbnail__badge73">73</span>
<div class="work-thumbnail js-img-error work-thumbnail--top work-thumbnail__topList">
<div class="work-thumbnail__topBd">
<a href="/coser/detail/54973/1193049" target="_blank" title="黄漫老师？不认识啦！！ 絮想长高五厘米">
<img src="https://img9.bcyimg.com/coser/54973/post/4boa/0806931030b211e78bbfc7294439e9ea.jpg/2X3" alt="埃罗芒阿老师 和泉纱雾 絮想长高五厘米">
</a>
</div>
<div class="work-thumbnail__ft center mt15 mb5">
<a href="/coser/detail/54973/1193049" target="_blank" title="黄漫老师？不认识啦！！ 絮想长高五厘米" class="cut db fz16 text">
黄漫老师？不认识啦！！ </a>
</div>
<div class="center cut">
<a href="/u/1033972" class="_avatar _avatar--user work-thumbnail__topavatar mr10 mt0"><img src="https://user.bcyimg.com/Public/Upload/avatar/1033972/bdb6186b9ffe4f7a9e16b8b698683ab4/small.jpg"></a>
<span class="fz12 lh24"><a href="/u/1033972">絮想长高五厘米</a></span>
</div>
</div>
</li>
"""""
soup = BeautifulSoup(html,'lxml')
print(soup.prettify())
print(soup.span.string)





