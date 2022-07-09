Title: Group Checks

{% from 'cta_top.html' import cta_top %} 
{{ cta_top("Group Monitoring Checks",
  "Group individual checks together and set down conditions for broader testing, alerting, reporting and incident resolution.",
  "{static}/images/Group_Checks_Monitor_Overall_Performance_x1000px.gif"
)}}

{% from 'banner.html' import banner %} 
{{ banner("The observability you've been waiting for",
  "Group monitoring checks by type, domain, geography, and more.",
  "bg-light-gray",
  "bg-success"
)}}

{% from 'image_block.html' import image_block %}
{{ image_block("left", "{static}/images/Group_Monitoring_Checks_Uptime_Performance_Tracking_Uptime.png",
"GROUP MONITORING CHECKS",
"Nest individual checks into groups",
"Get a bird’s-eye-view into system-wide uptime performance or custom groupings by service, customers, geographies and more.",
"bg-success") }}

{{ image_block("right", "{static}/images/Uptime_Report_for_Group_Checks_on_Website_System_Monitoring_Uptime.com.png",
"SYSTEM UPTIME TESTING",
"Check and correlate issues",
"Catch performance issues between services, components, and locations that could otherwise be missed. Quickly understand if other systems and sites are impacted.",
"bg-success") }}

{{ image_block("left", "{static}/images/GC_gif_1-1.gif",
"SYSTEM DOWNTIME NOTIFICATIONS",
"Alert on interrelated check failure",
"Configure precise alerting conditions that accurately notify IT and SRE stakeholders when a number of monitoring checks within a group go down.",
"bg-success") }}

{{ image_block("right", "{static}/images/Uptime_and_SLA_Reporting_Service_for_Group_Monitoring_Checks_Uptime.com.png",
"SYSTEM SLA PERFORMANCE",
"Report overall performance",
"Don’t just tag checks, deliver insights. Share uptime data on dozens – or thousands – of checks for dashboards, SLA reports, and status pages displaying a group’s overall performance or average SLA per check.",
"bg-success") }}

{{ image_block("left", "{static}/images/Website_Downtime_and_Incident_Data_for_Uptime_Monitoring_Uptime.com.png",
"SYSTEM INCIDENT RESOLUTION",
"Remove confusion from resolution",
"Delineate between isolated issues and system-wide outages. Arm support and engineering teams with precise incident data on impacted grouped or individual checks.",
"bg-success") }}


{% from 'testimonial.html' import testimonial %}
{{ testimonial("{static}/images/Feature_Rich_Monitoring_Tool_Uptime.com_User_Review_Pieter.webp",
  "bg-warning",
  "The one monitoring tool we have been waiting for.",
  "Feature-rich: good monitoring, good reporting, and fine live pages. SLA reporting is now a piece of cake, we deliver SaaS software - where uptime is a critical factor.")}}


{% from 'cta_bottom.html' import cta_bottom %} 
{{ cta_bottom("Group monitoring checks now",
  ("Associate individual checks together", 
  "Differentiate isolated vs. system-wide issues",
  "Customize thresholds and alerting",
  "Report on overall or average SLA values",
  "Display data in reports & status pages")
  )}}

