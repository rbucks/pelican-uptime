Title: Quickstart Guide

<div class="container bg-white my-5">
  <h1 class="mt-4 text-center">Website Uptime &amp; Performance Monitoring</h1>
  <h2 class="mb-4 text-center">Onboarding Quick Start Guide</h2>
  <hr class="my-5 bg-success w-50">

  <p class="subheading text-center">This guide covers the basics of our monitoring platform's functionality, and offers specifics for testing website performance.</p>
  <p class="subheading text-center">See our <a href="https://support.uptime.com/" target="_blank"> support articles</a> or <a href="https://uptime.com/contact?hsLang=en" target="_blank"> contact us </a> directly with questions.</p>

  <h2 class="mb-4 mt-5">Table of Contents</h4>
  <img class="float-right" title="Website Uptime Monitoring Software Onboarding Guide" src="{static}/images/Website_Uptime_Monitoring_Software_Onboarding_Guide.webp" alt="Website Uptime Monitoring Software Onboarding Guide" width="300" height="300" />
  <p class="subheading">1. <a href="#What_is_a_Check"> What is a Check? </a>  <br /> 2. <a href="#Creating_Your_First_Check"> Create Your First Check </a>  <br /> 3. <a href="#Using_Advanced_Checks"> Use Advanced Checks </a>  <br /> 4. <a href="#Setting_Up_Notifications"> Configure Performance Alerts </a>  <br /> 5. <a href="#Adding_Contacts_And_Contact_Groups"> Add Contacts and Contact Groups </a>  <br /> 6. <a href="#Adding_New_Users"> Add New Monitoring Users </a>  <br /> 7. <a href="#Understanding_Check_Failures"> Understand Check Failures </a>  <br /> 8. <a href="#Using_Reporting"> Use Web Monitoring Reports </a>  <br /> 9. <a href="#Visit_Our_Help_Desk"> Visit Our Help Desk </a> </p>
  
  
  <a id="What_is_a_Check" data-hs-anchor="true"></a>
  <h2 class="text-center mt-5">What is a Check?</h2>
  <hr class="my-5 bg-success w-50">
  <p class="subheading">A <strong> Check </strong> monitors a URL or IP address at intervals as low as 1-minute from various locations across six continents. When the URL or IP address fails, checks issue alerts that contain details of the downtime incident(s) to designated contacts.</p>
  <p class="subheading"><a href="https://support.uptime.com/hc/en-us/articles/115002533889-Overview-of-Checks" target="_blank"> This overview </a> covers the various check types available to you. See below for all monitoring checks available on Uptime.com:</p>
  <div class="row">
    <div class="col">
      <h3 class="mb-4" data-sr-id="14">Web</h3>
      <hr class="bg-success" />
      <p class="subheading"><img src="{static}/images/Uptime.com_Favicon.svg" alt="Uptime.com_Favicon" width="15" />  <a href="https://support.uptime.com/hc/en-us/articles/360001020389-HTTP-S-Check-Basics" target="_blank"> HTTP(S) </a></p>
      <p class="subheading"><img src="{static}/images/Uptime.com_Favicon.svg" alt="Uptime.com_Favicon" width="15" /> <a href="https://support.uptime.com/hc/en-us/articles/360000984785-Transaction-Check-Basics" target="_blank"> Transaction </a> </p>
      <p class="subheading"><img src="{static}/images/Uptime.com_Favicon.svg" alt="Uptime.com_Favicon" width="15" /> <a href="https://support.uptime.com/hc/en-us/articles/360001311589-API-Check-Basics" target="_blank"> API </a></p>
      <p class="subheading"><img src="{static}/images/Uptime.com_Favicon.svg" alt="Uptime.com_Favicon" width="15" />  <a href="https://support.uptime.com/hc/en-us/articles/4415869187346-RUM-Setup-and-Basics" target="_blank"> Real User Monitoring </a></p>
      <p class="subheading"><img src="{static}/images/Uptime.com_Favicon.svg" alt="Uptime.com_Favicon" width="15" />  <a href="https://support.uptime.com/hc/en-us/articles/5063344527004-Getting-Started-with-the-Uptime-com-Group-Check" target="_blank"> Group Checks </a></p>
      <p class="subheading"><img src="{static}/images/Uptime.com_Favicon.svg" alt="Uptime.com_Favicon" width="15" />  <a href="https://support.uptime.com/hc/en-us/articles/360001310925-Malware-Virus-Check-Basics" target="_blank"> Malware/Virus </a></p>
      <p class="subheading"><img src="{static}/images/Uptime.com_Favicon.svg" alt="Uptime.com_Favicon" width="15" /> <a href="https://support.uptime.com/hc/en-us/articles/360001349165-SSL-Certificate-Expiry-Check-Basics" target="_blank"> SSL Certificate/Expiry </a></p>
    </div>
    <div class="col">
      <h3 class="mb-4" data-sr-id="16">Network</h3>
      <hr class="bg-success" />
      <p class="subheading"><a href="https://support.uptime.com/hc/en-us/articles/360001349245-Whois-Domain-Expiry-Check-Basics"> <img src="{static}/images/Uptime.com_Favicon.svg" alt="Uptime.com_Favicon" width="15" />  </a> <a href="https://support.uptime.com/hc/en-us/articles/360001349245-Whois-Domain-Expiry-Check-Basics" target="_blank"> Domain Whois/Expiry </a></p>
      <p class="subheading"><a href="https://support.uptime.com/hc/en-us/articles/360001366189-DNS-Server-Check-Basics" target="_blank"> <img src="{static}/images/Uptime.com_Favicon.svg" alt="Uptime.com_Favicon" width="15" /> DNS </a></p>
      <p class="subheading"><a href="https://support.uptime.com/hc/en-us/articles/360001310905-Ping-ICMP-Check-Basics" target="_blank"> <img src="{static}/images/Uptime.com_Favicon.svg" alt="Uptime.com_Favicon" width="15" /> Ping (ICMP) </a></p>
      <p class="subheading"><a href="https://support.uptime.com/hc/en-us/articles/360005618719-NTP-Check-Basics" target="_blank"> <img src="{static}/images/Uptime.com_Favicon.svg" alt="Uptime.com_Favicon" width="15" /> NTP </a></p>
      <p class="subheading"><a href="https://support.uptime.com/hc/en-us/articles/360001241389-SSH-Check-Basics" target="_blank"> <img src="{static}/images/Uptime.com_Favicon.svg" alt="Uptime.com_Favicon" width="15" /> SSH </a></p>
      <p class="subheading"><a href="https://support.uptime.com/hc/en-us/articles/360001273005-TCP-UDP-Check-Basics" target="_blank"> <img src="{static}/images/Uptime.com_Favicon.svg" alt="Uptime.com_Favicon" width="15" /> TCP/UDP </a></p>
    </div>
    <div class="col">
      <h3 class="mb-4" data-sr-id="18">Email</h3>
      <hr class="bg-success" />
      <p class="subheading"><a href="https://support.uptime.com/hc/en-us/articles/360001242825-Email-Server-Check-Basics" target="_blank"> <img src="{static}/images/Uptime.com_Favicon.svg" alt="Uptime.com_Favicon" width="15" /> SMTP/POP/IMAP </a></p>
      <p class="subheading"><a href="https://support.uptime.com/hc/en-us/articles/360001307089-Domain-Blacklist-Check-Basics" target="_blank"> <img src="{static}/images/Uptime.com_Favicon.svg" alt="Uptime.com_Favicon" width="15" /> Domain Blacklist </a></p>
    </div>
    <div class="col">
      <h3 class="mb-4" data-sr-id="20">Custom Checks</h3>
      <hr class="bg-success" />
      <p class="subheading"><a href="https://support.uptime.com/hc/en-us/articles/360014269679-Custom-Checks-for-Process-Monitoring#incoming_webhook_setup" target="_blank"> <img src="{static}/images/Uptime.com_Favicon.svg" alt="Uptime.com_Favicon" width="15" /> Webhook </a></p>
      <p class="subheading"><a href="https://support.uptime.com/hc/en-us/articles/360014269679-Custom-Checks-for-Process-Monitoring#heartbeat_setup" target="_blank"> <img src="{static}/images/Uptime.com_Favicon.svg" alt="Uptime.com_Favicon" width="15" /> Heartbeat </a></p>
    </div>
  </div>
  
  <a id="Creating_Your_First_Check" data-hs-anchor="true"></a>
  <h2 class="text-center mt-5">Let's Get Started:</h2>
  <h2 class="text-center">Create Your First Check</h2>
  <hr class="my-5 bg-success w-50">
  <p class="subheading">Upon first logging in, you are prompted to monitor your entire site. Enter any URL and click <strong> Go. </strong></p>
  <p class="subheading">Uptime.com will run checks for your web server, DNS, blacklist/malware, and email.</p>
  <img src="{static}/images/Check_Domain_Uptime_and_Availability_with_Uptime.com.webp" alt="Check Domain Uptime and Availability with Uptime.com" class="img-fluid w-75 my-4" />
  <p class="subheading">Add these checks individually, or in bulk:</p>
  <img src="{static}/images/Monitor_Entire_Site_for_DNS_Uptime_Web_Server_Performance.webp" alt="Monitor Entire Site for DNS Uptime and Web Server Performance"class="img-fluid w-75 my-4" />
  <img src="{static}/images/Test_Website_Uptime_Checks_From_Global_Probe_Server_Locations_Uptime.com.webp" alt="Test Website Uptime Checks From Global Probe Server Locations with Uptime.com" class="img-fluid w-50 my-4 float-right" />
  <p class="subheading">Users can also click <strong> Add New </strong> and configure checks one by one from the Checks screen ( <strong> Monitoring&gt;Checks </strong> ) to add a new check. Start with an HTTP(S) check, but also explore each monitoring check type based on your needs. Change the check type via the <strong> Check Type </strong> dropdown menu to any of our <a href="https://support.uptime.com/hc/en-us/articles/115002533889-Overview-of-Checks#check_types" target="_blank"> available check types </a> .</p>
  <p class="subheading"><strong> Tip: </strong> When creating or editing a check, select a location from the dropdown and then click <strong> Run Test </strong> to verify settings are correct.</p>

  <p class="subheading">Select a <strong> Check Type </strong> to create any check, then fill in the required fields. Read our <a href="https://support.uptime.com/hc/en-us/articles/360001187805-Uptime-com-Check-Field-Explanations#optional-parameters" target="_blank"> Check Field Explanation </a> on required and optional parameters.</p>
  <img src="{static}/images/Test_HTTP(S)_SSL_Certificates_and_APIs_on_Website_Uptime.com_Checks.webp" alt="Test HTTP(S), SSL Certificates, and APIs on Website with Uptime.com Checks" class="img-fluid w-75 my-4" />
  <p class="subheading">This article on <a href="https://support.uptime.com/hc/en-us/articles/360000830260-Advanced-Check-Options" target="_blank"> Advanced Check Options </a> can help further customize checks to utilize:</p>
  <ul>
    <li><strong> Maintenance windows </strong> : Prevent a check from issuing an alert while the <a href="https://support.uptime.com/hc/en-us/articles/360000830260-Advanced-Check-Options#maint_window" target="_blank"> maintenance window </a> is active. More information on how alerts work in <a href="https://support.uptime.com/hc/en-us/articles/360000830260-Advanced-Check-Options#maintenance" target="_blank"> maintenance state </a> .</li>
    <li><a href="https://support.uptime.com/hc/en-us/articles/360000830260-Advanced-Check-Options#escalations" target="_blank"> <strong> Escalations </strong> </a> <strong> : </strong> Send an additional alert once a pre-configured amount of time has passed (such as 5-min or 1-hr).</li>
    <li><a href="https://support.uptime.com/hc/en-us/articles/360000830260-Advanced-Check-Options#sensitivity_timeout" target="_blank"> <strong> Sensitivity </strong> </a> <strong> : </strong> The number of probe servers that must go to CRITICAL status before a check issues an alert.</li>
    <li><a href="https://support.uptime.com/hc/en-us/articles/360000830260-Advanced-Check-Options#number_of_retries" target="_blank"> <strong> Number of retries </strong> </a> : The number of times a probe server will retry a check before it goes to CRITICAL status.</li>
  </ul>
  <p class="subheading">...and other options dependent on the check.</p>
  <p class="subheading">See our <a href="https://support.uptime.com/hc/en-us/articles/360001187805-Uptime-com-Check-Field-Explanations" target="_blank"> Check Field Explanation </a> article for a full breakdown of each parameter.</p>
  
  <a id="Using_Advanced_Checks" data-hs-anchor="true"></a>
  <h2>Use Advanced Monitoring Checks</h2>
  
  <p class="subheading">These features provide advanced monitoring functionality to simulate website user experiencesand observe real-time performance:</p>
  <ul>
    <li>
      <ul>
        <li><a href="https://support.uptime.com/hc/en-us/articles/4415882255506-RUM-Logic-and-Definitions" target="_blank"> Real User Monitoring </a> : Monitors the performance experience of visitors to your site.</li>
        <li><a href="https://support.uptime.com/hc/en-us/articles/360000984785-Synthetic-Monitoring-With-the-Uptime-com-Transaction-Check" target="_blank"> Transaction Checks </a> : Monitors web transactions on your site (e.g. login, registration etc.).</li>
        <li><a href="https://support.uptime.com/hc/en-us/articles/360001311589-API-Check-Basics" target="_blank"> API Checks </a> : Monitors API using multiple HTTP(S) requests.</li>
        <li><a href="https://support.uptime.com/hc/en-us/articles/5063344527004-Getting-Started-with-the-Uptime-com-Group-Check" target="_blank"> Group Checks </a> : Organize multiple checks to monitor systems, report on performance, and manage incident response.</li>
        <li><a href="https://support.uptime.com/hc/en-us/articles/360014269679-Custom-Checks-for-Process-Monitoring" target="_blank"> Custom Checks </a> : Monitors periodic jobs and processes, issuing alerts according to whether an action occurs or a heartbeat is not detected.</li>
      </ul>
    </li>
  </ul>
  <img src="{static}/images/Real_User_Monitoring_RUM_Page_Load_Trend_2.gif" alt="Real_User_Monitoring_RUM_Page_Load_Trend_2" width="100%" />
  
  <a id="Setting_Up_Notifications" data-hs-anchor="true"></a>
  <h2>Configure Performance Alerts</h2>
  
  <p class="subheading">Email, SMS, and voice call notifications are part of New User Setup, and are created for the primary account holder upon first login. These details form the <strong> Default </strong> contact. When creating your first check, it will be automatically assigned to this <strong> Default </strong> contact to receive alert notifications.</p>
  <p class="subheading">Along with email, SMS, and voice calls, we support most major third-party push notification providers that can receive incident alerts. The Uptime.com app on the <a href="https://itunes.apple.com/us/app/uptime-com-website-monitoring/id1176754968" target="_blank"> iOS App Store </a> and <a href="https://play.google.com/store/apps/details?id=com.apppartner.uptime.uptime" target="_blank"> Google Play </a> supports push notifications for alerts too.</p>
  <p class="subheading">With this <a href="https://support.uptime.com/hc/en-us/sections/115000857285-Push-Notifications" target="_blank"> list of Push Notification Integrations </a> ,send alerts and metrics to the tools you&rsquo;re already using to monitor uptime and resolve incidents.</p>
  <p class="subheading">Here are some ideas for <a href="https://support.uptime.com/hc/en-us/articles/360005117559-Creating-Responsive-Escalations-for-Downtime-Alerting" target="_blank"> creating responsive escalations </a> . <br /> <br /> Subscribe to <a href="https://status.uptime.com/" target="_blank"> Uptime.com's status page </a> to be notified in advance of changes to our probe server locations.</p>
  <span id="hs_cos_wrapper_widget_1656531685226_" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_linked_image" data-hs-cos-general-type="widget" data-hs-cos-type="linked_image"> <img class="hs-image-widget " title="Web_Monitoring_Integration_Partners_1000x854" src="{static}/images/Web_Monitoring_Integration_Partners_1000x854.gif" alt="Web_Monitoring_Integration_Partners_1000x854" /> 
  
  <a id="Adding_Contacts_And_Contact_Groups" data-hs-anchor="true"></a>
  <h2>Add Contacts and Contact Groups</h2>
  
  <p class="subheading">The <strong> Contact Screen </strong> is used to add new contacts or edit existing ones. Depending on how the contact is configured, individuals or contact groups associated with each contact will be notified of a downtime incident via:</p>
  <ul>
    <li>Email</li>
    <li>SMS message and/or phone call</li>
    <li><a href="https://support.uptime.com/hc/en-us/articles/115002534509-Overview-of-Push-Notifications" target="_blank"> Push notifications through a third-party provider </a></li>
    <li>Uptime.com&rsquo;s Mobile Application ( <a href="https://itunes.apple.com/us/app/uptime-com-website-monitoring/id1176754968" target="_blank"> iOS </a> and <a href="https://play.google.com/store/apps/details?id=com.apppartner.uptime.uptime" target="_blank"> Android </a> Available)</li>
  </ul>
  <p class="subheading">Along with a contact&rsquo;s <strong> Name, Email/Phone </strong> , and/or <strong> Integrations </strong> assigned, you can set on-call scheduling and see the number of <strong> Checks </strong> and <strong> Escalations </strong> configured. Access it via <strong> Notifications&gt;Contacts. </strong></p>
  <img src="{static}/images/Add_Website_Downtime_Alerts_Notifications_Escalations_Uptime.com.webp" alt="Add Website Downtime Alerts Notifications and Escalations with Uptime.com" width="100%" />
  
  <a id="Adding_New_Users" data-hs-anchor="true"></a>
  <h2>Add New Monitoring Users</h2>
  
  <img src="{static}/images/Add_Users_Uptime.com_Website_Uptime_Performance_Monitoring_Software_Platform.webp" alt="Add Users to Uptime.com Website Uptime Performance Monitoring Software Platform" width="100%" />
  <p class="subheading"><a href="https://support.uptime.com/hc/en-us/articles/115002535909-Managing-User-Accounts" target="_blank"> <strong> Users </strong> </a> generally have access to reports, and can log into the platform to: view checks (those with higher permission levels can edit/create new checks), receive emailed invoices, and <a href="https://support.uptime.com/hc/en-us/articles/360006291539-Uptime-com-Reporting" target="_blank"> reports </a> .</p>
  <p class="subheading">Click <strong> New User </strong> from the <a href="https://uptime.com/accounts/account-users?hsLang=en" target="_blank">  <strong> Users Page </strong> </a> . Add the user&rsquo;s first/last name, email, and time zone. Then, choose that user&rsquo;s account Access Level, and opt in/out of Two-Factor Authentication and hit <strong> Save </strong> .</p>
  <p class="subheading">Uptime.com will then send a verification email to the user to create a password.</p>
  
  <a id="Understanding_Check_Failures" data-hs-anchor="true"></a>
  <h2>Understand Check Failures</h2>
  
  <p class="subheading">When a check fails, an alert is delivered to designated contact groups along with other integrated systems via push notification. The alert contains the date, time, and location relevant to the outage.</p>
  <p class="subheading">Depending on the check typeand notification provider, other technical data may be included such as server information, unexpected strings,links to real-time analysis, and any configured notes.</p>
  <img src="{static}/images/Website_Down_Check_Alert_Results_Uptime.com.webp" alt="Website Down Check Alert Results with Uptime.com" width="100%" />
  <p class="subheading"><strong> Please note: </strong>  <a href="https://support.uptime.com/hc/en-us/articles/5063344527004-Getting-Started-with-the-Uptime-com-Group-Check"> Group Check </a> alerts will not contain locations relevant to the outage, only the configured down condition.</p>
  
  <a id="Using_Reporting" data-hs-anchor="true"></a>
  <h2>Use Web Monitoring Reports</h2>
  
  <p class="subheading">Use the <a href="https://uptime.com/alerting/alert-history?hsLang=en" target="_blank"> Alert History Screen </a> for a quick or detailed view of alerts issued when a monitoring check fails.</p>
  <img src="{static}/images/Website_Downtime_Failed_Check_Alert_History_Uptime.com.webp" alt="Website Downtime Failed Check Alert History with Uptime.com" width="100%" />
  <p class="subheading">You can <a href="https://support.uptime.com/hc/en-us/articles/360016256820-Setup-Instructions-for-your-Uptime-com-Status-Page" target="_blank"> build status pages </a> (see <a href="https://uptime.com/s/samplepsp?hsLang=en" target="_blank"> example </a> ), or create and schedule an SLA report for any number of checks.</p>
  <p class="subheading">If you have added a <a href="https://support.uptime.com/hc/en-us/articles/4415869187346-RUM-Setup-and-Basics" target="_blank"> Real User Monitoring </a> (RUM) check, <a href="https://support.uptime.com/hc/en-us/articles/4415874052242-RUM-Data-and-Reports" target="_blank"> you can view RUM reports </a> as well. <strong> NOTE: </strong> RUM Checks do require adding HTML code to your website. <a href="https://support.uptime.com/hc/en-us/articles/360006595219-Why-am-I-Not-Seeing-My-RUM-Data-" target="_blank"> See instructions here </a> .</p>
  <p class="subheading">Finally, showcase uptime monitoring performance to visitors by adding the <a href="https://uptime.com/devices/services/widget?hsLang=en" target="_blank"> Uptime.com widget </a> to your website.</p>
  <img src="{static}/images/Customize_Reporting_Dashboards_Website_Uptime_Performance_Uptime.com.webp" alt="Customize Reporting Dashboards for Website Uptime Performance with Uptime.com" width="100%" />
  <p class="subheading">Once checks have been added to your account, you will notice check cards appearing on your dashboard.</p>
  <p class="subheading"><a href="https://support.uptime.com/hc/en-us/articles/115002557925-Overview-of-Dashboard#customizing-your-dashboard" target="_blank"> Customize your dashboard </a> to filter which check cards appear, in what order, and other settings tailored to your preference.</p>
  <p class="subheading">These check cards offer detailed statistics on current state, response time, and uptime as a percentage:</p>
  <img src="{static}/images/Website_Uptime_Monitoring_Software_Dashboard_Uptime.com_Platform.webp" alt="Website Uptime Monitoring Software Dashboard in Uptime.com Platform" width="100%" />
  <p class="subheading">Users can configure <strong> SLA Reports </strong> or <strong> Schedule Reports </strong> to send at set intervals (ie: daily, weekly, monthly, quarterly, or yearly).</p>
  <img src="{static}/images/Scheduled_Reports_on_Website_SLA_Performance_through_Uptime.com_Monitoring_Software.webp" alt="Scheduled Reports on Website SLA Performance through Uptime.com Monitoring Software" width="100%" />
  <p class="subheading">Create your first SLA report by clicking <strong> Reports&gt;SLA Reports </strong> , then select <strong> New SLA Report </strong> . Edit any SLA report to add or remove checks (either by tag or individually), or change the <a href="https://support.uptime.com/hc/en-us/articles/360017118860-Creating-an-Uptime-com-SLA-Report-#displaying_and_sorting_checks" target="_blank"> logic </a> that determines how the report is rendered.</p>
  <p class="subheading">Download a PDF or XLS SLA report copy by clicking <strong> Reports&gt;SLA Reports </strong> , locate the report and then select <strong> Actions&gt; Download PDF </strong> , or <strong> Download XLS </strong> .</p>
  <p class="subheading">Schedule a Report by clicking <strong> Reports&gt;Scheduled Reports </strong> .</p>
  <p class="subheading">It is also possible to view an Uptime Report for a specific check, which provides a continuous granular view of domain uptime.</p>
  
  <a id="Visit_Our_Help_Desk" data-hs-anchor="true"></a>
  <h2>Visit Our Help Desk</h2>
  
  <p class="subheading">Our <a href="https://support.uptime.com/" target="_blank"> Support Documentation </a> covers Uptime.com&rsquo;s functionality in greater detail. Search our Help Desk for fast answers, and <a href="https://support.uptime.com/hc/en-us/requests/new" target="_blank"> Submit a Ticket </a> if you're unable to find them. We're available 24/7 to help.</p>
</div>