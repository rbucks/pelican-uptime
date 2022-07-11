Title: Financial Websites Uptime

{% from 'cta_top.html' import cta_top %} 
{{ cta_top("Uptime Monitoring for Financial Services Websites",
  "Because in your world, uptime is money.",
  "{static}/images/Finance_Banking_Industries_Trust_Uptime.com_Monitoring_Uptime_1150.webp"
)}}


{% from 'banner.html' import banner %} 
{{ banner("<span class='text-success'>$7,900</span> per minute",
  "is the cost to companies impacted by unplanned outages.",
  "bg-dark",
  "bg-success",
  "text-white"
)}}

 <div class="container bg-white my-5">
  {% include 'index_logos.html' %}
 </div>

{% from 'image_block.html' import image_block %}
{{ image_block("left", "{static}/images/Add_Website_Monitoring_Checks_HTTP(S)_SSL_Uptime.webp",
"UPTIME MONITORING CHECKS",
"Test institutional infrastructure",
"Monitor the performance of marketing sites, registration pages, and critical portals for tuition and knowledge sharing between students and staff.",
"bg-success") }}





{% from 'testimonial.html' import testimonial %}
{{ testimonial("{static}/images/Uptime.com_User_Review_for_Website_Uptime_Performance_Monitoring.webp",
  "bg-success",
  "Excellent monitoring service",
  "Monitoring public services is critical to proactive service delivery. Uptime has already enabled us to detect outages in near real-time so we can respond quickly and restore services before impact occurs.")}}


{% from 'cta_bottom.html' import cta_bottom %} 
{{ cta_bottom("Try before you buy, 100% free",
  ("Comprehensive uptime monitoring", 
  "Accurate, reliable IT alerts",
  "360° infrastructure reporting",
  "24/7 human support",
  "À la carte monitoring subscriptions")
  )}}