Title: Domain Health

<script type="module">
  import { h, Component, render } from 'https://unpkg.com/preact?module';
  import htm from 'https://unpkg.com/htm?module';

  // Initialize htm with Preact
  const html = htm.bind(h);

  function App (props) {
    return html`<h1>Hello World!</h1>`;
  }

  render(html`<${App} />`, document.getElementById('dcontent'));
</script>

<div class="body-marketing">
{% include 'free_tools_navigation.html' %}
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
  <div class="col-md-5 py-6">
          
  <h3 class="mb-4">Test global uptime for</h3>
  <div>
      <dl class="spaced">
        <dt>Remote IP</dt>
        <dd>See what IP your website is served from in a particular region.</dd>
        <dt>DNS Lookup</dt>
        <dd>Monitor how long  DNS name resolution took from start to finish.</dd>
        <dt>Connect</dt>
        <dd>Monitor how long it took for the TCP connection to your server to complete.</dd>
        <dt>Redirect Time</dt>
        <dd>Get the total time for how long all redirection steps (such as name lookup, connection, pre-transfer and transfer) took before the final transaction began.</dd>
        <dt>TLS Connect</dt>
        <dd>Monitor how long it took to complete the  SSL/SSH handshake to your server.</dd>
        <dt>Request Time</dt>
        <dd>Measure how long it took for file transfers to begin, including all pre-transfer commands and negotiations specific to the particular protocol(s) involved.</dd>
        <dt>First Byte</dt>
        <dd>See how long it took for the first byte to transfer, including the time the server needed to calculate the result.</dd>
        <dt>Total Time</dt>
        <dd>Get the total time it took to download the URL.</dd>
      </dl>
    </div>
    </div>
  </div>
   <div class="col-md-5 py-6">
   </div>
</div>
