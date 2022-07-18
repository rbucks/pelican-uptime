Title: Monitoring

{% from 'cta_top.html' import cta_top %}

{{ cta_top("Website Monitoring Checks",
  "Configure sophisticated uptime monitoring checks without sacrificing simplicity.",
  "{static}/images/Web_Monitoring_Software_1150x920.gif"
)}}

{% from 'banner.html' import banner %}
{{ banner("1 in 4 visitors",
  "will abandon your site for a competitor's after just one failed web transaction.",
  "bg-light-gray",
  "bg-warning"
)}}

{% from 'image_block.html' import image_block %}
{{ image_block("left", "{static}/images/Add_Web_Monitoring_Checks_900x1020.webp",
"WEBSITE UPTIME MONITORING",
"Check everything",
"Choose from dozens of checks that monitor everything related to the performance, health, and downtime of public and internal websites, applications, and services.",
"bg-warning") }}

{{ image_block("right", "{static}/images/Synthetic_Transaction_Monitoring_920x1000.gif",
"SYNTHETIC TRANSACTION MONITORING",
"Test forms and flows",
"Choose from dozens of checks that monitor everything related to the performance, health, and downtime of public and internal websites, applications, and services.",
"bg-warning") }}

{{ image_block("left", "{static}/images/Global_Monitoring_Probe_Severs_900x760_1.webp",
"EXTERNAL &amp; PRIVATE PROBE SERVERS",
"Monitor public and private sites",
"Reliably test public websites for speed and performance from hundreds of global monitoring locations -- while private probe servers monitor intranet apps or internal sites behind firewalls.",
"bg-warning") }}

{{ image_block("right", "{static}/images/Web_Dashboard_Notifications_1160x870_1.webp",
"WEBSITE PERFORMANCE REPORTING",
"Catch issues before they're incidents",
"Verifiably detect web outage or performance issues across your systems, and validate downtime results systemically to avoid false alarms across sites, apps, and more.",
"bg-warning") }}

{{ image_block("left", "{static}/images/Add_Web_Monitoring_Checks_900x1020.webp",
"WEBSITE PERFORMANCE REPORTING",
"Associate individual checks into groups",
"Get a bird’s-eye-view into the state of your system-wide uptime performance. Group monitoring checks by services and more to alert on the status of your systems. <a href='{filename}group-checks.md' target='_blank'>Learn more</a>.",
"bg-warning") }}

{{ image_block("right", "{static}/images/Uptime_Monitoring_Customer_Support_1160x684.webp",
"UPTIME MONITORING SUPPORT",
"Count on top-rated support",
"We've got your back. Our 100% human support team is rated web monitoring's best and available 24/7/365 so you spend less time finding help and more time solving problems.",
"bg-warning") }}

{% from 'testimonial.html' import testimonial %}
{{ testimonial("{static}/images/Uptime.com_User_Review_for_Website_Uptime_Performance_Monitoring_Mike.webp",
  "bg-success",
  "Clean and simple yet robust set of monitoring tools - from a very happy user!",
  "Don’t mistake their simplicity for lack of features. Their platform is extremely robust and they have features that allow monitoring on items I didn’t even know was possible.")}}

{% from 'cta_bottom.html' import cta_bottom %}
{{ cta_bottom("Check website performance now",
  ("Add monitoring checks in minutes",
  "Easily set up synthetic monitoring",
  "Test via external and private locations")
  )}}
