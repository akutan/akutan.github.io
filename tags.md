---
layout: page
title: Tags 

---

<div class="page-content wc-container">
	<div class="post">
		<h1>Tags</h1>  
          <ul class="fa-ul">
            {% assign tags = (site.tags | sort:0) %}
            {% for tag in tags %}
            <li><span class="fa-li"><i class="fas fa-tag"></i></span>
                    <a href="{{ '/tag/' | append: tag[0] | relative_url }}" data-toggle="tooltip" data-placement="right" title="{{ tag[1].size }}">
                <span>{{tag[0] }}</span></a></li>
            {% endfor %}
          </ul>
	</div>
</div>