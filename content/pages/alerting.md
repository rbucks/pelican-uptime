Title: Alerting

{% from 'cta_top.html' import cta_top %} 
{{ cta_top("Website Downtime Alerts",
  "Get immediate (and accurate) alert notifications before website issues become downtime outages.",
  "/images/Web_Downtime_Alerts_1150x920.gif"
)}}


{% from 'banner.html' import banner %} 
{{ banner("Conversion rates drop <span style='color: #f15d5e;'>4.42%</span>",
  "with every second of load time between 0-5 seconds.",
  "bg-light-gray",
  "bg-warning"
)}}


{% from 'image_block.html' import image_block %}
{{ image_block("left", "/images/Web_Downtime_Alert_Escalation_900x814.webp",
"DOWNTIME ALERT ESCALATIONS",
"Alert who you want, and how",
"Customize alerts across call, text, email, and popular DevOps tools. Designate contacts and set escalations by severity or seniority levels.",
"bg-danger") }}

{{ image_block("right", "/images/Web_Downtown_Alert_Notifications_950x800.webp",
"MULTI-CHANNEL INCIDENT ALERTS",
"Know when something goes wrong",
"Get moment-it-happens web downtime and performance alerts to any device or software tool you use and prefer. If you're notified -- it's for good reason.",
"bg-danger") }}

{{ image_block("left", "/images/Alerting_Maintenance_Schedule_960x1002.gif",
"ACCURATE WEB MONITORING ALERTS",
"Finally forget about false alarms",
"We double-check our web monitoring checks from multiple locations and won't alert you during designated windows to decrease false positives -- and increase a good night's sleep.",
"bg-danger") }}

{{ image_block("right", "/images/Web_Downtime_Traceroute_test_1150x618.webp",
"NETWORK TRACEROUTE DIAGNOSTICS",
"Quickly diagnose incidents",
"Efficiently detect downtime regionally, globally, and everywhere else. Get real-time check statuses to quickly delineate (and fix) local isolated incidents versus global outages.",
"bg-danger") }}

{{ image_block("left", "/images/Group_Monitoring_Checks_Uptime_Performance_Tracking_Uptime.png",
"GROUP WEB MONITORING ALERTS",
"Associate Individual Checks into Groups",
"Customize grouped monitoring checks with alert conditions. Easily structure alerts and escalations for teams and contacts. <a href='{filename}group-checks.md' target='_blank'>Learn more</a>.",
"bg-danger") }}

{{ image_block("right", "/images/Award_Winning_Web_Monitoring_Tools_890x750.webp",
"UPTIME MONITORING SUPPORT",
"Count on 100% human support",
"Like our platform, our people are always up. Trust the industry's top-rated technical support team to quickly resolve website downtime and performance issues.",
"bg-danger") }}


{% from 'testimonial.html' import testimonial %}
{{ testimonial("/images/No_False_Alarms_Matteo_Review.webp",
  "bg-danger",
  "Nothing to dislike: no false notifications",
  "A reliable service which can be configured with great simplicity to monitor any kind of website. Its alert system is able to notify you and trace issues immediately.")}}


{% from 'cta_bottom.html' import cta_bottom %} 
{{ cta_bottom("Configure downtime alerts now",
  ("Add alerts, escalations, comm channels", 
  "Notify accurately, avoid false IT alarms",
  "Diagnose and resolve web issues efficiently")
  )}}
