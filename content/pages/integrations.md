title: Site Uptime Integrations | Website Performance Monitoring
description: Website monitoring service. Easily deliver downtime alerts, response time metrics, and more website uptime and performance data to DevOps tools you trust.

{% from 'cta_top.html' import cta_top %} 
{{ cta_top("Uptime Monitoring Integrations",
  "Easily connect website performance data and alerts with the DevOps tools you know -- and trust.",
  "/images/Web_Monitoring_Integration_Partners_1150x986.gif"
)}}


{% from 'banner.html' import banner %} 
{{ banner("<span class='text-success'>20+</span> uptime integrations, <span class='text-success'>thousands</span> in use",
  "by monitoring customers at this very moment.",
  "bg-light-gray",
  "bg-success"
)}}


<div class="container bg-white my-5">
  <div class="card-deck mb-5">
    {% for logo in ("integrations_cachet.png", "integrations_datadog.png", "integrations_geckoboard.png", "integrations_jira_serviceDesk.png", "integrations_klipfolio.png", "integrations_librato.png") %}
    <div class="card bg-white text-white shadow">
      <img class="card-img my-auto p-4" src="/images/{{ logo }}">
      <div class="card-img-overlay">
      </div>
    </div>
     {% endfor %}
  </div>
  <div class="card-deck mb-5">
    {% for logo in ("integrations_microsoftTeams.png", "integrations_pagerduty.png", "integrations_pushbullet.png", "integrations_pushover.png", "integrations_signafi.png", "integrations_slack.png") %}
    <div class="card bg-white text-white shadow">
      <img class="card-img my-auto p-4" src="/images/{{ logo }}">
      <div class="card-img-overlay">
      </div>
    </div>
    {% endfor %}
  </div>
  <div class="card-deck mb-5">
    {% for logo in ("integrations_splunk.png", "integrations_status_io.png", "integrations_statuspage.png", "integrations_twitter.png", "integrations_wavefront.png", "integrations_zapier.png") %}
    <div class="card bg-white text-white shadow">
      <img class="card-img my-auto p-4" src="/images/{{ logo }}">
      <div class="card-img-overlay">
      </div>
    </div>
    {% endfor %}
  </div>
</div>


{% from 'image_block.html' import image_block %}
{{ image_block("left", "/images/Website_Uptime_Monitoring_Integrated_IT_Dashboards_1150x704.webp",
"WEBSITE REPORTING INTEGRATIONS",
"Deliver uptime data to dashboards",
"Seamlessly deliver your downtime alerts and response time metrics to the dashboard tools you’re already using.",
"bg-success") }}

{{ image_block("right", "/images/Integrated_Website_Performance_Monitoring_Downtime_Alerting_Slack_Microsoft_Teams_1150x700.webp",
"DOWNTIME ALERTING INTEGRATIONS",
"Manage alerts by tools and teams",
"Streamline the delivery and escalation of web outage alerts to the devices, software, and channels you communicate and resolve incidents with.",
"bg-success") }}

{{ image_block("left", "/images/Website_Status_Pages_Integrated_Uptime_Performance_Monitoring_Data_1150x1048.webp",
"WEBSITE STATUS PAGE INTEGRATIONS",
"Display system status page data",
"Automatically deliver downtime alerts and response time metrics for real-time updates to your web status pages.",
"bg-success") }}

{{ image_block("right", "/images/Uptime.com_API_Documentation_Website_Uptime_Performance_Monitoring_1100x1030.webp",
"UPTIME MONITORING DOCUMENTATION",
"Use our REST API for the rest",
"If you've already built your own system, ours easily fits in with data delivery, triggering actions, and programmatic system configuration and setup.",
"bg-success") }}

{{ image_block("right", "/images/Create_Website_Uptime_Performance_Monitoring_Integrations_with_Uptime.com_Zapier_1150x594.webp",
"CUSTOM UPTIME MONITORING INTEGRATIONS",
"Create integrations we don't have",
"We'll go as deep as your DevOps stack does. Our Zapier partnership puts another 3,000+ potential web uptime monitoring integrations at your fingertips.",
"bg-success") }}


{% from 'testimonial.html' import testimonial %}
{{ testimonial("/images/Platform_Integrations_Review_Alex_1000px.webp",
  "bg-success",
  "Uptime.com has a lot of integrations",
  "Uptime.com has a lot of integrations with other platforms (Slack, PagerDuty, etc.) and we have found that very helpful. Additionally we have found that they have a very good API as well as good documentation for how to use it.")}}


{% from 'cta_bottom.html' import cta_bottom %} 
{{ cta_bottom("Integrate your web monitoring now",
  ("Connect to DevOps tools you trust", 
  "Easily customize and alert IT contacts",
  "Deliver data for uptime reporting and status"),
  "bg-success"
  )}}
