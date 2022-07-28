Title: Status Pages

{% from 'cta_top.html' import cta_top %} 
{{ cta_top("Website &amp; System Status Pages",
  "Share unplanned incidents and scheduled updates with public and private audiences.",
  "/images/Web_Status_page_Tools_resize.gif"
)}}


{% from 'banner.html' import banner %} 
{{ banner("Websites average <span class='text-success'>3 hours</span> per month",
  "of downtime due to server overloads, DDoS attacks, and more.",
  "bg-light-gray",
  "bg-success"
)}}


{% from 'image_block.html' import image_block %}
{{ image_block("left", "/images/Website_Uptime_Monitoring_Status_Page_Builder_with_Uptime.com_1000x768.webp",
"WEBSITE PERFORMANCE MONITORING",
"Manage uptime and incidents",
"Easily communicate web outages with our status pages, or via integrations to status page tools you're already using -- your choice.",
"bg-muted") }}

{{ image_block("right", "/images/Custom_Website_Status_Page_Builder_Downtime_Communication_1160x834.webp",
"CUSTOM HOSTED STATUS PAGES",
"Create branded status pages",
"Build polished, fully customizable website status pages with impeccable data fidelity you'll actually want seen -- and subscribed to.",
"bg-muted") }}

{{ image_block("right", "/images/Subscribe_Web_Status_Page_1150x960.gif",
"SYSTEM STATUS PAGE SUBSCRIBERS",
"Publicly share external updates",
"Control content, appearance, timing, escalation, and alert actions to deliver external web status pages that fit precise communication use cases.",
"bg-muted") }}

{{ image_block("left", "/images/Private_Password_Protected_Website_Status_Pages_for_Outage_Communication_1150x680.webp",
"PRIVATE WEBSITE STATUS PAGES",
"Keep internal updates private",
"Keep employees, management, and teams aware of internal updates and scheduled maintenance windows with shareable secured status pages.",
"bg-muted") }}

{{ image_block("right", "/images/Sharable_Website_Status_Pages_Downtime_and_Outage_Communication_1150x742.webp",
"PUBLIC WEBSITE STATUS PAGES",
"Reduce pressure on IT and support",
"Lower the temperature and reduce angry support tickets for customer-facing teams by arming them with a single reference page to direct customers to.",
"bg-muted") }}

{{ image_block("left", "/images/Website_Performance_Monitoring_SLA_Status_Pages_150x816.webp",
"SLA PERFORMANCE STATUS PAGES",
"Turn incidents into trust",
"Accountability inspires credibility. Demonstrate yours to website visitors with historical SLA data on downtime, incidents, and performance.",
"bg-muted") }}


{% from 'testimonial.html' import testimonial %}
{{ testimonial("/images/Professional_Looking_Status_Page_Review_Rob_1000px.webp",
  "bg-success",
  "Great Monitoring Platform!",
  "The status pages are also fantastic so that we can put out a professional looking status page on our cloud services along with incident reporting. Combined with SAML logins for staff, and configurable alerts, and integration with our alert platform Opsgenie, this is one solid package for external monitoring.")}}


{% from 'cta_bottom.html' import cta_bottom %} 
{{ cta_bottom("Monitor website user experience now",
  ("Monitor and share uptime status in one tool", 
  "Deploy custom branded status pages",
  "Share public website status or keep private"),
  "bg-muted"
  )}}
