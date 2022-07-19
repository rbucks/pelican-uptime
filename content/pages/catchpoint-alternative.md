Title: Catchpoint Alternative

{% from 'cta_top.html' import cta_top %} 
{{ cta_top("Uptime.com is a top Catchpoint alternative",
  'Choose Uptime.com over Catchpoint for easier setup, better support, and no false alarms -- while paying 15% less for uptime monitoring.',
  "{static}/images/Catchpoint_Alternative_1150x920.gif"
)}}


 <div class="container bg-white my-5">
  {% include 'index_logos.html' %}
 </div>


{% from 'banner.html' import banner %} 
{{ banner("<span class='text-success'>Don't just take our word for it</span>",
  "See how we compare in functionality and user feedback.",
  "bg-light-gray",
  "bg-success"
)}}


{% from 'table_compare.html' import table_compare %} 
<div class="container bg-white my-5">
  {{ table_compare("Better Uptime",
    (
      ("Global External Monitoring", "✓", "✓"),
      ("Comprehensive Checks", "✓", ""),
      ("Synthetic Monitoring", "✓", "✓"),
      ("Real User Monitoring", "✓", "✓"),
      ("API Monitoring", "✓", "✓"),
      ("Private Locations", "✓", ""),
      ("System Status Pages", "✓", ""),
      ("Customizable Dashboard", "✓", "✓"),
      ("Integrations", "✓", "✓"),
      ("Subaccounts", "✓", ""),
      ("G2", "", ""),
      ("Ease of Use", "✓", ""),
      ("Ease of Setup", "✓", "✓"),
      ("Ease of Admin", "✓", ""),
      ("Ease of Working With", "✓", ""),
      ("Product Direction", "✓", "✓"),
      ("Quality of Support", "✓", ""),
      ("Multi-Site Monitoring", "✓", ""),
      ("Multi-Channel Alerting", "✓", "")
    )
  )}}
  <hr class="mt-5 bg-success">
</div>


{% from 'image_block.html' import image_block %}
{{ image_block("left", "{static}/images/Best_Website_Uptime_Monitoring_Services_with_Uptime.com_890x750.webp",
"TOP-RATED UPTIME MONITORING",
"Trusted to stay up",
"By thousands of customers who love the quality, stability, and reliability of our award-winning platform and people.

<br/><br/>By industry experts like G2 and TechRadar who have named us one of the world’s best web monitoring solutions.",
"bg-success") }}

{{ image_block("right", "{static}/images/Best_Customer_Support_Website_Uptime_Performance_Monitoring_Uptime.com1160x684.webp",
"UPTIME MONITORING SUPPORT",
"Trust our top-rated technical support",
"Products alone don't solve problems, people do. Our 100% human support team is rated the industry's best and available 24/7/365 to ensure you spend less time finding help and more time resolving incidents.",
"bg-success") }}

{{ image_block("left", "{static}/images/Add_HTTP(S)_Check_400x508.gif",
"WEBSITE PERFORMANCE MONITORING",
"Get used to ease of use",
"We easily beat Datadog in anything related to ease of use. Leverage dozens of checks like HTTP(S), SSL, synthetic monitoring, and RUM with the web monitor with the best usability ratings on G2.",
"bg-success") }}

{{ image_block("right", "{static}/images/Synthetic_Transaction_Check_Monitoring_for_Website_Forms_and_Shopping_Carts_with_Uptime.com_1150x668.webp",
"DOWNTIME MONITORING CHECKS",
"Take advantage of better monitoring",
"More money doesn't mean more monitoring. Utilize dozens of checks not found with Catchpoint to monitor the entirety of your websites, applications, and networks -- without breaking your budget.",
"bg-success") }}

{{ image_block("left", "{static}/images/Website_Downtime_Alert_Notification_Setup_Uptime.com_900x814.webp",
"DOWNTIME ALERT ESCALATIONS",
"Customize your monitoring, your way",
"Customize alerts across call, text, email, or any DevOps tool. Assign main contacts and teams, then designate when (and who) gets notified based on severity levels.",
"bg-success") }}

{{ image_block("right", "{static}/images/Best_Technical_Support_Team_for_Website_Uptime_Performance_Monitoring_with_Uptime.com_1100x796.webp",
"UPTIME MONITORING VALUE",
"If you've heard of us, it's for the right reasons",
"Stop paying more for less. Work with the top-rated web uptime service that enables users to buy what they need (and nothing they don't) while saving 10-15% annually on monitoring.",
"bg-success") }}


{% from 'testimonial_compare.html' import testimonial_compare %}
{{ testimonial_compare(
  ("{static}/images/Uptime.com_User_Review_Website_Uptime_Performance_Monitoring_Philippe.webp",
  "Uptime.com User Review",
  "Easy to reach and team members react very promptly.  Had an issue with an SSL certificate monitor and they addressed it quickly."),
  ("{static}/images/Catchpoint_User_Review_Website_Uptime_Performance_Monitoring_Shawn.webp",
  "Catchpoint User Review",
  "I DO NOT LIKE THAT IT IS DIFFICULT TO GET AHOLD OF (CATCHPOINT) CUSTOMER SERVICE.")
  )}}


{% from 'cta_bottom.html' import cta_bottom %} 
{{ cta_bottom("Try the best uptime, 100% free",
  ("No credit card required free trial", 
  "Flexible website monitoring subscriptions",
  "Top-rated uptime tools & support")
  )}}