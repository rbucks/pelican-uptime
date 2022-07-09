Title: Reporting

{% from 'cta_top.html' import cta_top %} 
{{ cta_top("Uptime Reporting & Analytics",
  "Report on website uptime, page speed, and SLA performance with anyone, anywhere, anytime. ",
  "{static}/images/Web_Reporting_Real_User_Monitoring_1150x920.gif"
)}}


{% from 'banner.html' import banner %} 
{{ banner("<span class='text-info'>8</span> in <span class='text-info'>10</span> web visitors",
  "won't return to a site with performance issues.",
  "bg-light-gray",
  "bg-info"
)}}


{% from 'image_block.html' import image_block %}
{{ image_block("left", "{static}/images/Web_Uptime_Dashboard_Monitoring_1100x840.webp",
"WEBSITE PERFORMANCE MONITORING",
"Design your ideal dashboards",
"Display critical uptime performance data via custom monitoring dashboards and reports by alerts, check types, and SLAs -- and segment by different users and teams.",
"bg-info") }}

{{ image_block("right", "{static}/images/New_Scheduled_Report_1150x920.gif",
"PERFORMANCE REPORT SCHEDULING",
"Decide who sees what, and when",
"Schedule reports on checks and systems you need; then deliver uptime monitoring data to the people and teams that need it via automated report links or API by day, week, month, quarter, or year -- you choose.",
"bg-info") }}

{{ image_block("left", "{static}/images/Page_Speed_Real_User_Monitoring_RUM_1150x748_2.webp",
"REAL USER MONITORING (RUM)",
"Go deeper with RUM",
"Don’t report on website performance without understanding website experience. Analyze real user website sessions to optimize site code, elements, and uptime. <a href='{filename}real-user-monitoring.md' target='_blank'>Learn more</a>.",
"bg-info") }}

{{ image_block("right", "{static}/images/Custom_Status_Pages_1160x834.webp",
"CUSTOM HOSTED STATUS PAGES",
"Report on uptime and incidents",
"Communicate downtime in the same tool you monitor uptime with. Create branded system status pages with impeccable data fidelity you'll want seen and subscribed to.",
"bg-info") }}

{{ image_block("left", "{static}/images/Group_Monitoring_Checks_Uptime_Performance_Tracking_Uptime.png",
"GROUP MONITORING CHECKS",
"Associate individual checks into groups",
"Group monitoring checks by services, customers, and geographies to report on the true state of your system’s uptime for SLA accountability. <a href='{filename}group-checks.md' target='_blank'>Learn more</a>",
"bg-info") }}


{% from 'testimonial.html' import testimonial %}
{{ testimonial("{static}/images/Artboard-1-copy-16_2x.webp",
  "bg-info",
  "Great insights",
  "Real fidelity in data, way more accurate than other services. Nothing so far I can point out as a bad thing. Improved my client's page speed a ton.")}}


{% from 'cta_bottom.html' import cta_bottom %} 
{{ cta_bottom("Report on website performance now",
  ("Fully customize uptime dashboards", 
  "Enable sharing, scheduling, delivery",
  "Monitor and report downtime together")
  )}}
