Title: Domain Health

<div class="body-marketing">
{% from 'free_tools_navigation.html' import free_tools_navigation %}
{{
  free_tools_navigation('health')
}}

{% from 'free_tools_top.html' import free_tools_top %}
{% from 'free_tools_number_of.html' import free_tools_number_of %}
{{
free_tools_top(
"WEBSITE PERFORMANCE MONITORING",
"Free domain health test for any website",
"Get peace of mind by monitoring your domain in its entirety, web, DNS, email, blacklist and more.",
'<form method="post" class="mb-6">
<input type="hidden" name="csrfmiddlewaretoken" value="ZCxmaIeYUrGWkCg3qdyhyzWoVIa0rMHw7POWr7TUd4UkVuhicoTVAzEKSyjyiAfq">

<div class="form-group">
<div class="input-group ">
<input type="text" name="url" class="form-control " value="http://">  
 <input type="hidden" name="abt_tm" value="1657875786">
<label style="display: none;"><input type="checkbox" name="abt_accept_terms" value="1">
I am an electronic being and I accept the terms &amp; conditions for electronic beings only.</label>

  <div class="input-group-append">
  <input type="submit" class="btn btn-secondary px-4" value="Start Testing">
   </div>
  </div>
  <div class="invalid-feedback d-block"></div>
</div>
    </form>',
    "{static}/images/FreeTools_Domain_Health_Test.gif",
    )

}}
{{
  free_tools_number_of(
    "# of domains analyzed (and counting)...",
    "ensure every facet of your site is up and operational.",
    0,
    373.37,
  )
}}

<div class="container">
  <div class="row">
  <div class="col-5 py-6">
          
  <h3 class="mb-4">Check domain health for</h3>
  <div class="mb-5">
    <h4 class="mb-4"><i class="heading-icon fal fa-sliders-h mr-3"></i> DNS</h4>
    <p class="mb-2">We run multiple tests against your DNS servers and their configuration, and alert you the instant a DNS issue is detected..</p>
    </div>
    <div class="mb-5">
      <h4 class="mb-4"><i class="heading-icon far fa-globe mr-3"></i> Web Server</h4>
        <p class="mb-2">Our monitoring checks test your website status every minute, and alert you the moment your web server’s status changes..</p>
    </div>
    <div class="mb-5">
      <h4 class="mb-4"><i class="heading-icon far fa-envelope mr-3"></i> Mail Server</h4>
        <p class="mb-2">We monitor email servers for each MX record with multiple performance checks, and alert you if there’s a problem..</p>
    </div>
    <div>
      <h4 class="mb-4"><i class="heading-icon far fa-bug mr-3"></i> Blacklist/Malware</h4>
        <p class="mb-2">We check 100+ Domain and IP Blacklists every day to ensure you’re not on one..</p>
    </div>
  </div>
   <div class="col-6 offset-1 py-6">
    {% from 'free_tools_recents_table.html' import free_tools_recents_table %}
    {{
      free_tools_recents_table(
        ["domain", "date", "error"],
      )
    }}
   </div>
  </div>
</div>
