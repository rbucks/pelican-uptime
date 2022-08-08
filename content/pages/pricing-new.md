Title: Pricing New

{% from 'table_pricing.html' import table_pricing %} 
<div class="container-fluid bg-very-light-gray pt-5">
  <div class="container pricing">
    <div class="row">
      <div class="col pt-4 mr-4">
        <h1>Plans &amp; Pricing</h1>
        <div class="row p-1 rounded" style="background-color: #E5E5E5;">
          <div class="col"><span class="btn btn-outline btn-sm border-0">MONTHLY</span></div>
          <div class="col"><span class="btn btn-outline btn-sm btn-success">ANNUALLY</span></div>
        </div>
      </div>
      <div class="col p-4 mx-4">
        <h2>Essential</h2>
        <p class="mb-2">Start low and grow.</p>
        <p class="light">Common features and usage, add à la carte forever.</p>
        <p class="from">From <span class="price">$79/mo.</span></p>
        <div class="btn btn-success w-100">Try For Free</div>
      </div>
      <div class="col p-4 highlighted mx-4">
        <h2>Premium</h2>
        <p class="mb-2">Feature-proof and flexible.</p>
        <p class="light">Premium features and usage, save 20% forever.</p>
        <p class="from">From <span class="price">$499/mo.</span></p>
        <div class="btn btn-success w-100">Try For Free</div>
      </div>
      <div class="col p-4 ml-4">
        <h2>Custom</h2>
        <p class="mb-2">Address complex needs.</p>
        <p class="light">Create your monitoring experience.</p>
        <p class="from">From <span class="price">$999/mo.</span></p>
        <div class="btn btn-success w-100">Let's Talk</div>
      </div>
    </div>
    <div class="row text-center my-5">
      <div class="col">
        <h2 class="mb-0 upgrade">Upgrade to 14-day Free Trial</h2>
        <img src="{static}/images/upgrade_underline.svg" style="margin-top: -32px;"/>
        <p class="light" style="margin-top: -13px;">No credit card required -- cancel anytime.</p>
      </div>
    </div>
    <div class="row">
      <table class="table table-responsive table-striped table-borderless mx-auto text-center w-75 new-pricing mb-5">
        <thead>
          <tr>
            <th scope="col" class="header text-left pt-4 pb-3">Key Features</th>
            <th scope="col" style="width: 15%">Essential</th>
            <th scope="col" style="width: 15%">Premium</th>
            <th scope="col" style="width: 15%">Custom</th>
          </tr>
        </thead>
        <tbody>
          {{ table_pricing("Monitoring for HTTP(S), SSL, DNS, & more",
            '<img src="{static}/images/pricing-new-no.svg" alt="X icon">',
            '<img src="{static}/images/pricing-new-no.svg" alt="X icon">',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">'
          )}}
          {{ table_pricing("Transaction, RUM, API, heartbeat, & webhook checks",
            '<img src="{static}/images/pricing-new-no.svg" alt="X icon">',
            '<img src="{static}/images/pricing-new-no.svg" alt="X icon">',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">'
          )}}
          {{ table_pricing("Alerts via SMS, phone, email, & integrations",
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">'
          )}}
          {{ table_pricing("Unlimited monitoring integrations",
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">'
          )}}
          {{ table_pricing("Status pages & scheduled reports",
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">'
          )}}
          {{ table_pricing("More checks, alerts, & features",
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">'
          )}}
          {{ table_pricing("20% off future à la carte add-ons",
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">'
          )}}
        </tbody>
        <thead>
          <tr>
            <th scope="col" class="header text-left pt-4 pb-3">Uptime Monitoring</th>
            <th scope="col"></th>
            <th scope="col"></th>
            <th scope="col"></th>
          </tr>
        </thead>
        <tbody>
          {{ table_pricing('Basic Monitoring Checks <p class="subheading mt-2">Continuously test website, network, and email server performance.</p>',
            '30+',
            '200+',
            'Customize'
          )}}
          {{ table_pricing('Transaction Checks <p class="subheading mt-2">Mimic user actions to test flows and forms via synthetic monitoring.</p>',
            '3+',
            '15+',
            'Customize'
          )}}
          {{ table_pricing('Group Checks <p class="subheading mt-2">Organize multiple checks to monitor systems, report on performance, and manage incident response. Receive alerts when group failure conditions are met.</p>',
            '1+',
            '5+',
            'Customize'
          )}}
          {{ table_pricing('Real User Monitoring Requests (Page & Ajax Views) <p class="subheading mt-2">Monitor speed, errors, and performance with user data.</p>',
            '200,000+',
            '2,000,000+',
            'Customize'
          )}}
          {{ table_pricing('API Checks <p class="subheading mt-2">Test APIs with multiple HTTP(S) requests, custom headers and tokens.</p>',
            '3+',
            '20+',
            'Customize'
          )}}
          {{ table_pricing('Custom Checks <p class="subheading mt-2">Monitor processes with cron jobs, heartbeats, and webhooks.</p>',
            '3+',
            '20+',
            'Customize'
          )}}
          {{ table_pricing('REST API <p class="subheading mt-2">Manage your monitoring account without logging in.</p>',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            'Customize'
          )}}
          {{ table_pricing('Basic Monitoring Checks <p class="subheading mt-2">Continuously test website, network, and email server performance.</p>',
            '30+',
            '200+',
            'Customize'
          )}}
          {{ table_pricing('Basic Monitoring Checks <p class="subheading mt-2">Continuously test website, network, and email server performance.</p>',
            '30+',
            '200+',
            'Customize'
          )}}
        </tbody>
        <thead>
          <tr>
            <th scope="col" class="header text-left pt-4 pb-3">Alerts</th>
            <th scope="col"></th>
            <th scope="col"></th>
            <th scope="col"></th>
          </tr>
        </thead>
        <tbody>
          {{ table_pricing('Monthly SMS Credits <p class="subheading mt-2">Get text message alert notifications.</p>',
            '180+',
            '800+',
            'Customize'
          )}}
          {{ table_pricing('Monthly Phone Credits <p class="subheading mt-2">Get automated call alert notifications.</p>',
            '18+',
            '80+',
            'Customize'
          )}}
          {{ table_pricing('Email Notifications <p class="subheading mt-2">Get alert notifications delivered to your inbox.	</p>',
            'Unlimited',
            'Unlimited',
            'Customize'
          )}}
          {{ table_pricing('Third-Party Integrations <p class="subheading mt-2">Use Uptime.com with popular DevOps tools.</p>',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            'Customize'
          )}}
        </tbody>
        <thead>
          <tr>
            <th scope="col" class="header text-left pt-4 pb-3">Reports &amp; SLAs</th>
            <th scope="col"></th>
            <th scope="col"></th>
            <th scope="col"></th>
          </tr>
        </thead>
        <tbody>
          {{ table_pricing('Dashboards <p class="subheading mt-2">Customize for downtime, alerts, and check reporting.	</p>',
            '2+',
            '10+',
            'Customize'
          )}}
          {{ table_pricing('Scheduled SLA Reports <p class="subheading mt-2">Deliver checks, systems, and SLA response reports to designated contacts.</p>',
            '2+',
            '10+',
            'Customize'
          )}}
        </tbody>
        <thead>
          <tr>
            <th scope="col" class="header text-left pt-4 pb-3">Status Pages</th>
            <th scope="col"></th>
            <th scope="col"></th>
            <th scope="col"></th>
          </tr>
        </thead>
        <tbody>
          {{ table_pricing('System Status Pages <p class="subheading mt-2">Create external and internal pages for incident communication.</p>',
            '1+',
            '5+',
            'Customize'
          )}}
          {{ table_pricing('Status Page Subscribers <p class="subheading mt-2">The total available subscriber seats across status pages.</p>',
            '250+',
            '1,000+',
            'Customize'
          )}}
        </tbody>
        <thead>
          <tr>
            <th scope="col" class="header text-left pt-4 pb-3">Account &amp; Settings</th>
            <th scope="col"></th>
            <th scope="col"></th>
            <th scope="col"></th>
          </tr>
        </thead>
        <tbody>
          {{ table_pricing('20% off à la carte usage <p class="subheading mt-2">Available with Premium subscription only, learn more.</p>',
            '<img src="{static}/images/pricing-new-no.svg" alt="X icon">',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            'Customize'
          )}}
          {{ table_pricing('User Accounts <p class="subheading mt-2">The total number of available platform login seats.</p>',
            '1+',
            'Unlimited',
            'Customize'
          )}}
          {{ table_pricing('Historical Data Retention <p class="subheading mt-2">Retain alert history and RUM averages.</p>',
            '6mo',
            '24mo',
            'Customize'
          )}}
          {{ table_pricing('Subaccounts <p class="subheading mt-2">Segment monitoring accounts for different users and teams.</p>',
            '<img src="{static}/images/pricing-new-no.svg" alt="X icon">',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            'Customize'
          )}}
          {{ table_pricing('Private Monitoring Locations <p class="subheading mt-2">Test intranet apps or sites behind firewalls.	</p>',
            '<img src="{static}/images/pricing-new-no.svg" alt="X icon">',
            'Add-on',
            'Customize'
          )}}
          {{ table_pricing('Single Sign-On <p class="subheading mt-2">View your account’s history and changes.</p>',
            '<img src="{static}/images/pricing-new-no.svg" alt="X icon">',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            'Customize'
          )}}
          {{ table_pricing('Traceroute <p class="subheading mt-2">Detect anomalies between an Uptime.com probe server and your website.</p>',
            '<img src="{static}/images/pricing-new-no.svg" alt="X icon">',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            'Customize'
          )}}
          {{ table_pricing('Premium Support <p class="subheading mt-2">Get fast response and resolution with our technical experts.	</p>',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            'Customize'
          )}}
          {{ table_pricing('Enterprise Account Management <p class="subheading mt-2">Get custom support, QBRs, strategy and more.</p>',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            '<img src="{static}/images/pricing-new-yes.svg" alt="checkmark icon">',
            'Customize'
          )}}
        </tbody>
      </table>
    </div>
  </div>
</div>
<div class="container-fluid p-5" style="background: #F2FBF7;">
  <h2 class="text-center my-5">Trusted By Thousands</h2>
  {% include 'badges.html' %}
  <div class="container">
    <div class="row mb-5">
      <div class="col bg-white mr-4 p-5">
        <img src="{static}/images/Capterra_with_stars.svg" style="max-height: 40px;">
        <div class="d-flex mt-2">
          <div class="pr-1"><img src="{static}/images/Capterra_star_full.svg" style="max-height: 48px;"></div>
          <div class="px-1"><img src="{static}/images/Capterra_star_full.svg" style="max-height: 48px;"></div>
          <div class="px-1"><img src="{static}/images/Capterra_star_full.svg" style="max-height: 48px;"></div>
          <div class="px-1"><img src="{static}/images/Capterra_star_full.svg" style="max-height: 48px;"></div>
          <div class="pl-1"><img src="{static}/images/Capterra_star_half.svg" style="max-height: 48px;"></div>
        </div>
      </div>
      <div class="col bg-white ml-4 p-5">
        <img src="{static}/images/Trustpilot_with_stars.svg" style="max-height: 40px;">
        <div class="d-flex mt-2">
          <div class="pr-1"><img src="{static}/images/Trustpilot_star_full.svg" style="max-height: 48px;"></div>
          <div class="px-1"><img src="{static}/images/Trustpilot_star_full.svg" style="max-height: 48px;"></div>
          <div class="px-1"><img src="{static}/images/Trustpilot_star_full.svg" style="max-height: 48px;"></div>
          <div class="px-1"><img src="{static}/images/Trustpilot_star_full.svg" style="max-height: 48px;"></div>
          <div class="pl-1"><img src="{static}/images/Trustpilot_star_full.svg" style="max-height: 48px;"></div>
        </div>
      </div>
    </div>
  </div>
</div>
<div class="container-fluid bg-very-light-gray pt-5">
  <div class="container">
    <h2 class="text-center my-5 py-3">Reviews and Testimonials</h2>
    <div class="container px-5">
      <div class="row bg-white">
        <div class="col p-5">
          {% from 'pricing_review.html' import pricing_review %}
          {{ pricing_review('Perfect monitoring provider',
              '5',
              '04/01/22',
              'We have tested a few solutions and uptime.com is the best in price performance. The transactions and checks are easy to configure and it is a pleasure to work with. Alerting is available via e-mail, sms, and also phonecall. It monitors everything from real user monitoring, to transactions and certificates.',
              'https://uptime.com'
            )}}
          {{ pricing_review('Perfect monitoring provider',
              '5',
              '04/01/22',
              'We have tested a few solutions and uptime.com is the best in price performance. The transactions and checks are easy to configure and it is a pleasure to work with. Alerting is available via e-mail, sms, and also phonecall. It monitors everything from real user monitoring, to transactions and certificates.',
              'https://uptime.com'
            )}} 
          {{ pricing_review('Perfect monitoring provider',
              '5',
              '04/01/22',
              'We have tested a few solutions and uptime.com is the best in price performance. The transactions and checks are easy to configure and it is a pleasure to work with. Alerting is available via e-mail, sms, and also phonecall. It monitors everything from real user monitoring, to transactions and certificates.',
              'https://uptime.com'
            )}} 
          {{ pricing_review('Perfect monitoring provider',
              '5',
              '04/01/22',
              'We have tested a few solutions and uptime.com is the best in price performance. The transactions and checks are easy to configure and it is a pleasure to work with. Alerting is available via e-mail, sms, and also phonecall. It monitors everything from real user monitoring, to transactions and certificates.',
              'https://uptime.com'
            )}} 
          {{ pricing_review('Perfect monitoring provider',
              '5',
              '04/01/22',
              'We have tested a few solutions and uptime.com is the best in price performance. The transactions and checks are easy to configure and it is a pleasure to work with. Alerting is available via e-mail, sms, and also phonecall. It monitors everything from real user monitoring, to transactions and certificates.',
              'https://uptime.com'
            )}}      
        </div>
      </div>
    </div>
  </div>
</div>
<div class="container-fluid bg-very-light-gray">
  <div class="container pt-5">
    <h2 class="text-center py-5">Frequently Asked Questions</h2>
    <div id="accordion">
      {% from 'faq.html' import faq %} 
      {{ faq("1",
            "Why offer flexible monitoring subscriptions?",
            '<p>Because we pride ourselves on listening to our users.</p>
            <p>"Quick and helpful customer support, but pricing plans could be more dynamic." - G2 Review</p>
            <p>This change has been advocated for by customers and employees. More flexible, less bundled subscriptions allow you to add/customize usage in a self-serve capacity without upgrading to a higher plan tier or going through Sales.</p>'
      )}}
      {{ faq("2",
            "You say you’re flexible yet offer 3 different subscriptions? Explain.",
            '<p>SaaS plans involve multiple fixed package options that vary by features and price. The fixed nature of these plans require users to upgrade to a higher tier if they’ve reached their maximum feature or volume limits.</p>
            <p>Our subscription levels are preset with starting features + volume minimums. Users select a level with the base price, features, and volume they need and add features/capacity from there.</p>'
      )}}
      {{ faq("3",
            "Are discounts available to annual subscribers at any level?",
            '<p>Yes. 15% discounts are applied to accounts on annual subscriptions. Users who select our Premium subscription level when signing up for the first time receive 20% off future à la carte usage.</p>'
      )}}
      {{ faq("4",
            "Can I add-on your $449/mo Premium level after my initial subscription?",
            '<p>Yes, this will grant you access to more advanced features like Audit Log, SSO, Private Locations, and Subaccounts.</p>
            <p>However, adding Premium monitoring at a later date means your account is ineligible for the 20% à la carte discount or higher usage minimums. We strongly encourage users anticipating incremental usage to start at the Premium level when first subscribing to lock-in future savings as needs grow.</p>'
      )}}
      {{ faq("5",
            "Do you enable à la carte downgrades as well as upgrades?",
            '<p>Downgrades must be managed by our <a href="mailto:support@uptime.com">Support staff</a> to protect against system abuse and violations. Submit a <a href="/contact?">support ticket</a> to get started.</p>'
      )}}
      {{ faq("6",
            "Any features not available à la carte via the Subscription Tool?",
            '<p>Uptime.com subaccounts and Private Monitoring Locations require <a href="mailto:support@uptime.com">Support</a> configuration and aren’t available self-serve at this time. Both are set up within 24 business hours of a ticketed request.</p>'
      )}}
      {{ faq("7",
            "What about existing customers on a legacy fixed plan?",
            '<p>They have the same flexibility and self-serve access that new users have, and can add incremental website monitoring features as their uptime needs grow.</p>'
      )}}
      {{ faq("8",
            "Where can I find the self-serve Subscription Tool?",
            '<p>It’s easily found within Uptime.com’s website monitoring user panel, under: Billing → Subscription.</p>'
      )}}
      <br/><br/>
    </div>
  </div>
</div>