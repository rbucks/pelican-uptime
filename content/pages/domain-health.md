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
    "<div id=\"dcontent\"></div>",
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
</div>
