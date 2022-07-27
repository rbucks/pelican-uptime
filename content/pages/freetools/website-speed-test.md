Title: Free Website Speed Test - Try our Page Speed Tool
<!-- slug: website-speed-test
save_as: freetools/website-speed-test.html -->
status: draft

<div class="body-marketing">


{% from 'free_tools_navigation.html' import free_tools_navigation %}
{{
  free_tools_navigation('speed')
}}

{% from 'free_tools_top.html' import free_tools_top %}

{{
free_tools_top(
"WEBSITE SPEED MONITORING",
"Free speed test for any website",
"Enter your website’s URL to see how fast your site loads from a global location of your choice.",
'<form method="post" class="mb-6">
<input type="hidden" name="csrfmiddlewaretoken" value="ZCxmaIeYUrGWkCg3qdyhyzWoVIa0rMHw7POWr7TUd4UkVuhicoTVAzEKSyjyiAfq">

<div class="form-group">
<div class="input-group ">
 <input type="text" name="url" class="form-control " value="http://"> 
 <input type="hidden" name="abt_tm" value="1657875786">
<label style="display: none;"><input type="checkbox" name="abt_accept_terms" value="1">
I am an electronic being and I accept the terms &amp; conditions for electronic beings only.</label>

<select name="location" class="form-control" style="max-width: 180px;">
      <option value="">Random location</option>
      <option value="3">Amsterdam, Netherlands</option>
      <option value="13">Dallas, USA</option>
      <option value="5">Frankfurt, Germany</option>
      <option value="7">London, United Kingdom</option>
      <option value="8">New York, USA</option>
      <option value="14">San Francisco, USA</option>
      <option value="10">Singapore</option>
      <option value="11">Sydney, Australia</option>
      <option value="12">Tokyo, Japan</option>
  </select>
  <div class="input-group-append">
  <input type="submit" class="btn btn-secondary px-4" value="Start Testing">
   </div>
  </div>
  <div class="invalid-feedback d-block"></div>
</div>
    </form>',
    "{static}/images/FreeTools_Website_Speed_Test.gif",
    )

}}


{% from 'free_tools_number_of.html' import free_tools_number_of %}
{{
  free_tools_number_of(
    "# of pages analyzed (and counting)...",
    "ensure your site is optimized for the speed visitors expect.",
    231000000,
    1767.34,
  )
}}


<div class="container">
  <div class="row">
    <div class="col-md-5 py-6">
      <h3 class="mb-4">Page speed matters to your</h3>
      <div class="mb-5">
        <h4 class="mb-3"><i class="heading-icon far fa-eye mr-3"></i> Visitors</h4>
        <p>Who admit taking only ~50 milliseconds to decide whether to stay or bounce from your site.</p>
      </div>
      <div class="mb-5">
        <h4 class="mb-3"><i class="heading-icon far fa-shopping-cart mr-3"></i> Customers</h4>
        <p>70% of who admit page speed impacts their willingness to buy online.</p>
      </div>
      <div class="mb-5">
        <h4 class="mb-3"><i class="heading-icon far fa-search mr-3"></i> Search Engines</h4>
        <p>Who take loading speed into account as an important SEO factor. </p>
      </div>
      <div class="mb-5">
        <h4 class="mb-3"><i class="heading-icon far fa-users mr-3"></i> Teammates</h4>
        <p>Who monitor loading speed, analyze performance, and use insights to improve website code.</p>
      </div>
    </div>
   <div class="col-6 offset-1 py-6">
    {% from 'free_tools_recents_table.html' import free_tools_recents_table %}
    {{
      free_tools_recents_table(
        ["domain", "date", "load time"],
      )
    }}
   </div>
  </div>
</div>

</div>
