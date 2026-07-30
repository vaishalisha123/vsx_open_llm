# =====================================================
# VisionScaleX Static Knowledge
# =====================================================
import re

def get_static_response(query):

    query = query.lower().strip()

    for keywords, response in STATIC_KNOWLEDGE:

        for keyword in keywords:

            pattern = r"\b" + re.escape(keyword.lower()) + r"\b"

            if re.search(pattern, query):

                return response

    return None
# ----------------------------
# Greeting
# ----------------------------

GREETING_KEYWORDS = [

    "hi",
    "hello",
    "hey",
    "hii",
    "hiii",
    "hey there",
    "hello there",
    "good morning",
    "good afternoon",
    "good evening",
    "greetings",
    "yo"

]

GREETING_RESPONSE = """
Hi! 👋 Welcome to VisionScaleX.

I'm your AI Assistant.

I can help you with:

• Services
• Industries
• Pricing
• Framework
• Company Information
• Contact Details
• Book a Demo

How can I assist you today?
"""


# ----------------------------
# Services
# ----------------------------

SERVICE_KEYWORDS = [

    "service",
    "services",
    "solution",
    "solutions",
    "offer",
    "offers",
    "offering",
    "provide",
    "provides",
    "providing",
    "what do you do",
    "what can you do",
    "what do you provide",
    "how can you help",
    "capabilities"

]

SERVICE_RESPONSE = """
VisionScaleX provides:

• AI-Powered Go-To-Market Strategy

• AI SDR Automation

• Revenue Intelligence

• Buying Signal Intelligence

• Personalized Cold Email Campaigns

• Account Research

• Account Enrichment

• Ideal Customer Profile (ICP) Development

• Ownership Mapping

• CRM Integration

• Workflow Automation

• Revenue Operations (RevOps) Consulting

• Executive Outreach

• Account-Based Marketing

• Qualified Executive Meeting Generation

• Proprietary Deal Origination

• Mandate Sourcing

If you'd like to know more about any specific service, just ask.
"""
# ----------------------------
# Pricing
# ----------------------------

PRICING_KEYWORDS = [

    "price",
    "pricing",
    "cost",
    "costing",
    "charges",
    "charge",
    "fees",
    "fee",
    "plans",
    "plan",
    "package",
    "packages",
    "subscription",
    "quote",
    "quotation",
    "estimate",
    "budget",
    "pricing model",
    "pricing plans",
    "custom pricing",
    "enterprise pricing",
    "how much",
    "how much does it cost",
    "what does it cost",
    "what is the cost",
    "what is the price",
    "pricing details",
    "pricing information",
    "pricing structure",
    "can i get pricing",
    "can i get a quote",
    "request pricing",
    "price list",
    "rate",
    "rates",
    "commercials",
    "commercial proposal",
    "proposal"

]

PRICING_RESPONSE = """
VisionScaleX offers customized pricing based on your business requirements.

Pricing depends on factors such as:

• Services required
• Business objectives
• Target market
• Outreach volume
• Automation requirements
• Data and intelligence needs
• Project scope

For a personalized quotation or pricing discussion, please contact our team:

📧 sales@visionscalex.com

🌐 www.visionscalex.com

Our team will understand your requirements and recommend the most suitable solution.
"""
# ----------------------------
# Mission | Vision | Philosophy
# ----------------------------

MISSION_KEYWORDS = [

    "mission",
    "vision",
    "vision statement",
    "mission statement",
    "goal",
    "goals",
    "objective",
    "objectives",
    "purpose",
    "company purpose",
    "our purpose",
    "why visionscalex",
    "why do you exist",
    "why was visionscalex founded",
    "what do you stand for",
    "what drives you",
    "core values",
    "values",
    "company values",
    "belief",
    "beliefs",
    "philosophy",
    "company philosophy",
    "business philosophy",
    "principles",
    "guiding principles",
    "ethics",
    "culture",
    "company culture",
    "long term vision",
    "future vision",
    "future goals",
    "future plans",
    "roadmap",
    "company roadmap",
    "where are you headed",
    "what is your vision",
    "what is your mission",
    "what are your goals",
    "tell me about your mission",
    "tell me about your vision",
    "tell me about your philosophy",
    "what is visionscalex mission",
    "what is visionscalex vision",
    "visionscalex values"

]

MISSION_RESPONSE = """
Mission

To transform strategic vision and investment theses into predictable, high-converting revenue pipelines and proprietary deal flow.

Vision

To become a trusted AI-powered growth partner helping businesses scale through intelligent Go-To-Market strategies, commercial intelligence, and automation.

Core Philosophy

We believe sustainable business growth should never depend on guesswork or mass outreach.

Organizations achieve better commercial outcomes by engaging the right companies, at the right time, with the right intelligence.

VisionScaleX combines Artificial Intelligence, commercial intelligence, automation, and human expertise to help businesses execute smarter, scalable, and data-driven Go-To-Market strategies.
"""
# ----------------------------
# Contact | Sales | Demo
# ----------------------------

CONTACT_KEYWORDS = [

    "contact",
    "contact us",
    "contact details",
    "contact information",
    "reach",
    "reach out",
    "get in touch",
    "connect",
    "talk to us",
    "talk to sales",
    "sales",
    "sales team",
    "support",
    "customer support",
    "help",
    "assistance",
    "email",
    "mail",
    "email address",
    "phone",
    "phone number",
    "mobile",
    "call",
    "telephone",
    "website",
    "official website",
    "consultation",
    "meeting",
    "appointment",
    "office",
    "office address",
    "address",
    "location",
    "head office",
    "headquarters",
    "hq",
    "how can i contact",
    "how do i contact",
    "how do i reach you",
    "where are you located",
    "where is your office",
    "contact number",
    "sales contact",
    "contact details please",
    "give me your email"

]

CONTACT_RESPONSE = """
You can reach the VisionScaleX team through the following channels:

📧 Sales Email
sales@visionscalex.com

🌐 Website
https://www.visionscalex.com

📞 Phone Numbers

United States
+1 262 245 8736

United Kingdom
+44 744 1427 052

India
+91 83750 30573

🤝 Book a Demo

Contact our team to schedule a personalized demonstration and discuss your business requirements.

Whether you're looking for AI-powered Go-To-Market solutions, Revenue Intelligence, AI SDR Automation, Workflow Automation, or strategic consulting, our experts will be happy to assist you.
"""

# ----------------------------
# Framework | Methodology | Process
# ----------------------------

FRAMEWORK_KEYWORDS = [

    "framework",
    "frameworks",
    "methodology",
    "process",
    "workflow",
    "workflows",
    "approach",
    "strategy",
    "execution",
    "implementation",
    "how do you work",
    "how does it work",
    "how it works",
    "how do you deliver",
    "working process",
    "working methodology",
    "delivery process",
    "delivery model",
    "operating model",
    "gtm framework",
    "sales framework",
    "business framework",
    "your framework",
    "visionscalex framework",
    "framework model",
    "operating process",
    "engagement process",
    "implementation process",
    "how do you help clients",
    "how do you execute projects",
    "project execution",
    "your methodology",
    "your process"

]

FRAMEWORK_RESPONSE = """
VisionScaleX follows a structured AI-powered Go-To-Market (GTM) framework designed to generate predictable revenue growth and high-quality business opportunities.

Our framework typically includes:

• Business Discovery & Goal Alignment

• Ideal Customer Profile (ICP) Development

• Target Account Identification

• Account Research & Intelligence

• Buying Signal Detection

• Data Enrichment & Ownership Mapping

• AI-Powered Personalized Outreach

• Multi-Channel Campaign Execution

• CRM Integration & Workflow Automation

• Meeting Generation & Pipeline Development

• Performance Tracking & Revenue Intelligence

• Continuous Optimization based on campaign insights and analytics

Every engagement is customized according to the client's business objectives, target market, and growth strategy.
"""
# ----------------------------
# Technology | AI Stack
# ----------------------------

TECHNOLOGY_KEYWORDS = [

    "technology",
    "technologies",
    "tech stack",
    "stack",
    "ai",
    "artificial intelligence",
    "machine learning",
    "ml",
    "llm",
    "large language model",
    "language model",
    "automation",
    "ai automation",
    "workflow automation",
    "platform",
    "software",
    "tools",
    "tool",
    "integrations",
    "integration",
    "crm",
    "crm integration",
    "api",
    "apis",
    "cloud",
    "data",
    "analytics",
    "revenue intelligence",
    "buying signals",
    "personalization",
    "email automation",
    "what technology do you use",
    "what technologies do you use",
    "what is your tech stack",
    "how does your ai work",
    "do you use ai",
    "what ai models do you use",
    "how does visionscalex work",
    "technical capabilities",
    "technical stack"

]

TECHNOLOGY_RESPONSE = """
VisionScaleX combines Artificial Intelligence, commercial intelligence, automation, and modern software technologies to help organizations accelerate revenue growth.

Our capabilities include:

• Artificial Intelligence (AI)

• Large Language Models (LLMs)

• AI SDR Automation

• Revenue Intelligence

• Buying Signal Intelligence

• Account Research & Enrichment

• Ideal Customer Profile (ICP) Development

• Ownership Mapping

• CRM Integration

• Workflow Automation

• Personalized Outreach

• Multi-Channel Campaign Automation

• Executive Outreach

• Account-Based Marketing (ABM)

• Performance Analytics & Reporting

Our technology stack is continuously evolving to deliver intelligent, scalable, and data-driven Go-To-Market solutions tailored to each client's business needs.
"""
# ----------------------------
# Why VisionScaleX | USP
# ----------------------------

USP_KEYWORDS = [

    "why visionscalex",
    "why choose visionscalex",
    "why choose you",
    "why should i choose you",
    "why should we choose you",
    "why work with visionscalex",
    "why work with you",
    "why your company",
    "why your services",
    "why are you different",
    "what makes you different",
    "difference",
    "different",
    "unique",
    "uniqueness",
    "usp",
    "unique selling proposition",
    "competitive advantage",
    "advantages",
    "benefits",
    "strengths",
    "key strengths",
    "why should i work with visionscalex",
    "why should my company choose visionscalex",
    "why partner with visionscalex",
    "why partner with you",
    "why your solution",
    "compare visionscalex",
    "competitors",
    "better than competitors",
    "why are you better"

]

USP_RESPONSE = """
VisionScaleX combines Artificial Intelligence, commercial intelligence, automation, and human expertise to help organizations build predictable and scalable revenue pipelines.

What makes VisionScaleX different:

• AI-powered Go-To-Market (GTM) strategy tailored to business objectives.

• Commercial intelligence that identifies the right companies, buyers, and buying signals.

• Personalized outreach instead of generic mass campaigns.

• End-to-end sales execution—from research and enrichment to meeting generation.

• CRM integration and workflow automation for higher operational efficiency.

• Revenue-focused approach designed to deliver measurable business outcomes.

• Customized solutions rather than one-size-fits-all services.

• Strategic partnership focused on long-term growth, not just lead generation.

Our objective is to help organizations reach the right decision-makers, accelerate sales cycles, and create sustainable revenue growth through intelligent, data-driven execution.
"""
# ----------------------------
# Demo | Consultation | Meeting
# ----------------------------

DEMO_KEYWORDS = [

    "demo",
    "book demo",
    "book a demo",
    "book the demo",
    "schedule demo",
    "schedule a demo",
    "schedule the demo",
    "request demo",
    "free demo",
    "live demo",
    "consultation",
    "book consultation",
    "book a consultation",
    "book the consultation",
    "schedule consultation",
    "schedule a consultation",
    "schedule the consultation",
    "consult",
    "meeting",
    "book meeting",
    "book a meeting",
    "book the meeting",
    "schedule meeting",
    "schedule a meeting",
    "schedule the meeting",
    "arrange meeting",
    "arrange a meeting",
    "arrange the meeting",
    "arrange meet",
    "arrange a meet",
    "arrange the meet",
    "appointment",
    "book appointment",
    "book a appointment",
    "book the appointment",
    "talk to sales",
    "sales call",
    "contact sales",
    "speak to sales",
    "sales team",
    "connect with sales",
    "business inquiry",
    "business enquiries",
    "business enquiry",
    "partnership discussion",
    "get started",
    "start project",
    "work with visionscalex",
    "hire visionscalex",
    "lets work together",
    "let's work together",
    "how do i get started",
    "how can i start",
    "how to begin",
    "interested",
    "i am interested",
    "we are interested",
    "how can I book a meeting",
    "how do I reach your team"

]

DEMO_RESPONSE = """
Thank you for your interest in VisionScaleX.

We would be happy to understand your business goals and discuss how our AI-powered Go-To-Market solutions can support your growth.

📅 Schedule a Meeting:

https://outlook.office.com/bookwithme/user/4d67eabae98d4606b1cce3fbbf367e9d@visionscalex.com/meetingtype/5VD52oCw7k-e2X4GwOw5Qw2?anonymous&ismsaljsauthenabled&ep=mLinkFromTile

📧 Sales Email:
sales@visionscalex.com

🌐 Website:
www.visionscalex.com

📞 Contact Numbers:

🇺🇸 US
+1 262 245 8736

🇬🇧 UK
+44 744 1427 052

🇮🇳 India
+91 8375030573

During the consultation, our team can discuss:

• Your business goals

• Current Go-To-Market challenges

• Target market and ICP

• AI automation opportunities

• Recommended VisionScaleX solutions

• Customized implementation roadmap

We look forward to helping your business grow with AI-powered revenue solutions.
"""
INDUSTRY_KEYWORDS = [

    "industry",
    "industries",
    "sector",
    "sectors",
    "domain",
    "domains",
    "market",
    "markets",

    "who do you serve",
    "who do you work with",
    "who are your clients",
    "who are your customers",
    "customer industries",
    "target industries",
    "business sectors",

    "which industries",
    "what industries",
    "which sectors",
    "what sectors",

    "do you work with startups",
    "startup",

    "enterprise",

    "small business",
    "sme",
    "mid market",

    "b2b",

    "technology",
    "saas",

    "healthcare",

    "finance",
    "fintech",

    "manufacturing",

    "consulting",

    "education",
    "edtech",

    "real estate",

    "ecommerce",

    "retail",

    "logistics",

    "telecom",

    "energy",

    "automotive",

    "professional services"
]
INDUSTRY_RESPONSE = """
VisionScaleX supports organizations across multiple industries by combining AI, commercial intelligence, and Go-To-Market expertise.

We commonly work with:

• Technology Companies

• SaaS Businesses

• AI Startups

• FinTech

• Healthcare

• Manufacturing

• Professional Services

• Consulting Firms

• Real Estate

• Retail & E-commerce

• Logistics & Supply Chain

• Telecommunications

• Education & EdTech

• Energy

• Automotive

• B2B Enterprises

Our solutions are customized according to each organization's:

• Business model

• Target market

• Ideal Customer Profile (ICP)

• Sales process

• Revenue objectives

Whether you're an early-stage startup or a global enterprise, VisionScaleX helps build predictable revenue pipelines using AI-powered Go-To-Market strategies.
"""
# =====================================================
# CASE STUDIES / EXPERIENCE / PORTFOLIO
# =====================================================

CASE_STUDIES = [

    "case study",
    "case studies",
    "success story",
    "success stories",
    "client success",
    "results",
    "achievements",
    "portfolio",
    "projects",
    "previous work",
    "work examples",
    "examples",
    "experience",
    "past clients",
    "customers",
    "companies worked with",
    "who have you worked with",
    "do you have experience",
    "industry experience",
    "track record",
    "proof",
    "proof of work",
    "performance",
    "business outcomes",
    "client outcomes",
    "impact",
    "what results have you delivered",
    "show me your work"

]


CASE_STUDIES_RESPONSE = """
VisionScaleX has experience helping businesses improve their Go-To-Market execution through AI, commercial intelligence, and revenue operations.

Our engagements typically focus on:

• AI-powered GTM Strategy
• Revenue Intelligence
• Buying Signal Intelligence
• AI SDR Automation
• Personalized Outreach Campaigns
• CRM & Workflow Automation
• Account Research & Enrichment
• Executive Meeting Generation
• Proprietary Deal Origination

Due to client confidentiality, detailed engagement information and case studies are shared during qualified business discussions.

To discuss similar use cases or request relevant examples, please contact our team.

📧 sales@visionscalex.com

🌐 www.visionscalex.com
"""
ABOUT_KEYWORDS = [

    "about",
    "about company",
    "about visionscalex",
    "company",
    "company info",
    "company information",
    "company profile",
    "introduction",
    "introduce yourself",
    "who are you",
    "what is visionscalex",
    "tell me about visionscalex",
    "tell me about your company",
    "business overview",
    "overview",
    "organization",
    "firm",
    "startup",
    "who is visionscalex",
    "visionscalex overview",
    "visionscalex company"

]


ABOUT_RESPONSE = """
VisionScaleX is an AI-powered Go-To-Market (GTM) and Revenue Intelligence company that helps organizations accelerate growth through intelligent automation, commercial intelligence, and data-driven execution.

We combine Artificial Intelligence, automation, market intelligence, and human expertise to help businesses:

• Generate qualified sales opportunities
• Improve outbound performance
• Identify high-value buying signals
• Build accurate Ideal Customer Profiles (ICP)
• Automate revenue workflows
• Improve sales productivity
• Create predictable revenue pipelines
• Source strategic business opportunities

Our solutions are designed for startups, growing businesses, enterprises, investors, and advisory firms looking to scale faster with AI-powered GTM execution.

Website:
https://visionscalex.com
"""
AI_SDR_KEYWORDS = [

    "ai sdr",
    "sdr",
    "sales development representative",
    "sales automation",
    "lead generation",
    "prospecting",
    "prospect",
    "cold email",
    "cold outreach",
    "email outreach",
    "outbound",
    "outbound sales",
    "sales outreach",
    "appointment setting",
    "meeting generation",
    "qualified meetings",
    "lead qualification",
    "sales pipeline",
    "pipeline generation",
    "outreach automation",
    "automated outreach",
    "sales engagement"

]


AI_SDR_RESPONSE = """
VisionScaleX's AI SDR Automation helps businesses scale outbound sales through intelligent automation while maintaining personalized engagement.

Our AI SDR capabilities include:

• Prospect Identification

• Ideal Customer Profile (ICP) Matching

• Account Research

• Buying Signal Detection

• Personalized Cold Email Generation

• Multi-Step Outreach Sequences

• Executive Contact Discovery

• Lead Qualification

• Meeting Scheduling

• CRM Synchronization

• Performance Tracking & Analytics

Our objective is to help sales teams spend less time on manual prospecting and more time engaging qualified opportunities.
"""
# =====================================================
# REVENUE INTELLIGENCE
# =====================================================

REVENUE_INTELLIGENCE_KEYWORDS = [

    "revenue intelligence",
    "revenue",
    "sales intelligence",
    "pipeline intelligence",
    "pipeline visibility",
    "revenue analytics",
    "sales analytics",
    "sales insights",
    "business intelligence",
    "commercial intelligence",
    "forecasting",
    "sales forecasting",
    "pipeline",
    "revenue growth",
    "sales growth",
    "performance insights",
    "revenue optimization",
    "sales performance",
    "opportunity intelligence",
    "what is revenue intelligence",
    "tell me about revenue intelligence",
    "explain revenue intelligence"

]


REVENUE_INTELLIGENCE_RESPONSE = """
VisionScaleX's Revenue Intelligence solutions help organizations make smarter sales decisions using AI-powered commercial insights and data-driven analytics.

Our Revenue Intelligence capabilities include:

• Sales Pipeline Visibility

• Opportunity Prioritization

• Buying Signal Analysis

• Customer & Account Intelligence

• Sales Performance Analytics

• Revenue Forecasting Support

• Executive-Level Insights

• CRM Data Intelligence

• Pipeline Optimization

• Actionable Growth Recommendations

By combining AI, automation, and commercial intelligence, VisionScaleX enables businesses to identify high-value opportunities, improve forecasting accuracy, optimize sales execution, and accelerate predictable revenue growth.
"""
# =====================================================
# BUYING SIGNAL INTELLIGENCE
# =====================================================

BUYING_SIGNAL_KEYWORDS = [

    "buying signal",
    "buying signals",
    "buyer intent",
    "intent data",
    "intent",
    "intent signals",
    "purchase intent",
    "sales signals",
    "lead signals",
    "prospect signals",
    "market signals",
    "account signals",
    "trigger events",
    "buying intent",
    "customer intent",
    "decision signals",
    "decision makers",
    "opportunity signals",
    "high intent leads",
    "sales opportunities",
    "warm leads",
    "qualified leads",
    "what are buying signals",
    "tell me about buying signals",
    "explain buying signal intelligence",
    "buying signal intelligence"

]


BUYING_SIGNAL_RESPONSE = """
VisionScaleX's Buying Signal Intelligence helps organizations identify prospects that are most likely to purchase by analyzing commercial signals and market activity.

Our Buying Signal Intelligence capabilities include:

• Intent Signal Identification

• High-Potential Account Discovery

• Market Activity Monitoring

• Opportunity Prioritization

• Decision-Maker Identification

• Prospect Qualification

• Sales Trigger Detection

• AI-Powered Commercial Intelligence

• Revenue Opportunity Insights

• Targeted Outreach Recommendations

By focusing on organizations that are actively showing buying intent, businesses can improve conversion rates, reduce wasted outreach, and engage prospects at the right time with the right message.
"""
# =====================================================
# PERSONALIZED COLD EMAIL CAMPAIGNS
# =====================================================

COLD_EMAIL_KEYWORDS = [

    "cold email",
    "cold emails",
    "cold emailing",
    "cold email campaign",
    "cold email campaigns",
    "email campaign",
    "email campaigns",
    "email outreach",
    "outreach",
    "personalized outreach",
    "email personalization",
    "personalized emails",
    "sales emails",
    "b2b outreach",
    "prospecting emails",
    "outbound emails",
    "automated email",
    "email automation",
    "email sequence",
    "email sequences",
    "drip campaign",
    "drip campaigns",
    "outbound campaign",
    "lead outreach",
    "prospect outreach",
    "how do your email campaigns work",
    "do you provide cold emailing",
    "tell me about cold email campaigns",
    "personalized cold email campaigns"

]


COLD_EMAIL_RESPONSE = """
VisionScaleX helps organizations engage decision-makers through highly personalized AI-powered cold email campaigns.

Our Cold Email Campaign capabilities include:

• AI-Powered Email Personalization

• Prospect Research

• ICP-Based Targeting

• Personalized Subject Lines

• Multi-Step Email Sequences

• Executive-Level Outreach

• Buying Signal-Based Messaging

• Automated Campaign Execution

• Performance Tracking & Optimization

• Continuous Campaign Improvement

Instead of sending generic bulk emails, VisionScaleX creates personalized outreach campaigns based on each prospect's business, industry, and potential needs—helping improve engagement, reply rates, and qualified meeting generation.
"""
# =====================================================
# ACCOUNT RESEARCH
# =====================================================

ACCOUNT_RESEARCH_KEYWORDS = [

    "account research",
    "research",
    "company research",
    "prospect research",
    "lead research",
    "business research",
    "organization research",
    "target account",
    "target account research",
    "account intelligence",
    "company intelligence",
    "business intelligence",
    "prospect intelligence",
    "company profiling",
    "account profiling",
    "client research",
    "market research",
    "account analysis",
    "company analysis",
    "research prospects",
    "research companies",
    "target companies",
    "company information",
    "business information",
    "prospect analysis",
    "customer research",
    "target research",
    "tell me about account research",
    "what is account research",
    "explain account research"

]


ACCOUNT_RESEARCH_RESPONSE = """
VisionScaleX provides AI-powered Account Research to help organizations identify and understand high-value target companies before initiating outreach.

Our Account Research capabilities include:

• Company Profiling

• Business & Industry Analysis

• Revenue & Growth Insights

• Decision-Maker Identification

• Organizational Structure Analysis

• Technology & Digital Footprint Research

• Buying Signal Identification

• Competitor Intelligence

• Market Position Analysis

• AI-Assisted Research Automation

Our research enables sales teams to approach prospects with relevant business context, resulting in more personalized conversations, stronger engagement, and higher conversion rates.
"""
# =====================================================
# ACCOUNT ENRICHMENT
# =====================================================

ACCOUNT_ENRICHMENT_KEYWORDS = [

    "account enrichment",
    "enrichment",
    "data enrichment",
    "lead enrichment",
    "contact enrichment",
    "company enrichment",
    "account data",
    "company data",
    "business data",
    "contact data",
    "prospect enrichment",
    "customer enrichment",
    "company profile",
    "lead data",
    "account information",
    "company information",
    "contact discovery",
    "contact verification",
    "business verification",
    "email verification",
    "data quality",
    "crm enrichment",
    "database enrichment",
    "prospect data",
    "firmographic data",
    "company insights",
    "what is account enrichment",
    "tell me about account enrichment",
    "explain account enrichment"

]


ACCOUNT_ENRICHMENT_RESPONSE = """
VisionScaleX provides AI-powered Account Enrichment to transform basic prospect information into rich, actionable business intelligence.

Our Account Enrichment capabilities include:

• Company Profile Enhancement

• Contact & Decision-Maker Discovery

• Email & Contact Verification

• Firmographic Enrichment

• Industry Classification

• Revenue & Employee Insights

• Technology Stack Identification

• Geographic & Market Intelligence

• CRM Data Enrichment

• AI-Powered Data Validation

By enriching prospect and account data, VisionScaleX enables businesses to improve targeting accuracy, personalize outreach, and increase sales efficiency with reliable, up-to-date information.
"""
# =====================================================
# IDEAL CUSTOMER PROFILE (ICP) DEVELOPMENT
# =====================================================

ICP_KEYWORDS = [

    "icp",
    "ideal customer profile",
    "customer profile",
    "ideal client profile",
    "ideal customer",
    "ideal client",
    "target customer",
    "target client",
    "customer segmentation",
    "market segmentation",
    "target audience",
    "buyer profile",
    "buyer persona",
    "customer persona",
    "persona",
    "target accounts",
    "target companies",
    "qualified prospects",
    "prospect profiling",
    "customer targeting",
    "account targeting",
    "target market",
    "how do you build an icp",
    "what is icp",
    "explain icp",
    "tell me about icp",
    "icp development",
    "ideal customer profile development"

]


ICP_RESPONSE = """
VisionScaleX helps organizations build data-driven Ideal Customer Profiles (ICP) to improve sales efficiency and maximize revenue opportunities.

Our ICP Development process includes:

• Business & Market Analysis

• Customer Segmentation

• Industry Prioritization

• Company Size Identification

• Geographic Targeting

• Revenue & Growth Criteria

• Technology Stack Analysis

• Buying Behavior Analysis

• Decision-Maker Identification

• AI-Powered Prospect Scoring

A well-defined ICP helps organizations:

• Focus on high-value prospects

• Improve lead quality

• Increase conversion rates

• Personalize outreach

• Reduce customer acquisition costs

• Build predictable revenue pipelines

VisionScaleX combines AI, commercial intelligence, and market research to create ICPs tailored to each organization's business objectives and Go-To-Market strategy.
"""
# =====================================================
# OWNERSHIP MAPPING
# =====================================================

OWNERSHIP_MAPPING_KEYWORDS = [

    "ownership mapping",
    "ownership",
    "ownership structure",
    "company ownership",
    "corporate structure",
    "organization structure",
    "ownership hierarchy",
    "company hierarchy",
    "parent company",
    "subsidiary",
    "subsidiaries",
    "holding company",
    "ownership analysis",
    "corporate ownership",
    "company relationships",
    "business ownership",
    "shareholding",
    "shareholders",
    "ownership intelligence",
    "ownership research",
    "decision makers",
    "decision maker mapping",
    "stakeholders",
    "stakeholder mapping",
    "key stakeholders",
    "organizational hierarchy",
    "corporate hierarchy",
    "business hierarchy",
    "who owns the company",
    "company ownership data",
    "ownership information",
    "tell me about ownership mapping",
    "what is ownership mapping",
    "explain ownership mapping"

]


OWNERSHIP_MAPPING_RESPONSE = """
VisionScaleX provides AI-powered Ownership Mapping to help organizations understand corporate ownership structures and identify key stakeholders within target accounts.

Our Ownership Mapping capabilities include:

• Parent & Subsidiary Identification

• Corporate Ownership Structure Analysis

• Shareholder & Investor Mapping

• Decision-Maker Identification

• Executive Leadership Mapping

• Business Unit Relationships

• Organizational Hierarchy Analysis

• Corporate Group Intelligence

• Stakeholder Identification

• AI-Powered Relationship Mapping

Ownership Mapping enables businesses to understand complex organizational structures, identify the right decision-makers, prioritize strategic accounts, and improve the effectiveness of enterprise sales and partnership initiatives.
"""
# =====================================================
# WORKFLOW AUTOMATION
# =====================================================

WORKFLOW_AUTOMATION_KEYWORDS = [

    "workflow",
    "workflow automation",
    "automation",
    "business automation",
    "process automation",
    "sales automation",
    "marketing automation",
    "crm automation",
    "email automation",
    "lead automation",
    "task automation",
    "business process automation",
    "workflow management",
    "automated workflow",
    "automation services",
    "automation solutions",
    "digital automation",
    "business workflow",
    "automate workflow",
    "workflow optimization",
    "workflow management system",
    "workflow solution",
    "workflow software",
    "automated process",
    "process optimization",
    "sales workflow",
    "marketing workflow",
    "operations automation",
    "internal workflow",
    "workflow integration",
    "intelligent automation",
    "ai automation",
    "ai workflow",
    "automation consulting",
    "workflow consulting",
    "what is workflow automation",
    "tell me about workflow automation",
    "explain workflow automation"

]


WORKFLOW_AUTOMATION_RESPONSE = """
VisionScaleX provides AI-powered Workflow Automation solutions that streamline business operations, reduce manual effort, and improve overall productivity.

Our Workflow Automation capabilities include:

• Sales Workflow Automation

• CRM Workflow Automation

• Lead Routing & Assignment

• Email & Communication Automation

• Task & Activity Automation

• Business Process Automation

• Multi-System Integration

• Approval Workflow Automation

• Data Synchronization

• AI-Driven Process Optimization

Our automation solutions help organizations:

• Reduce repetitive manual work

• Improve operational efficiency

• Minimize human errors

• Accelerate business processes

• Increase team productivity

• Enable scalable business growth

VisionScaleX combines AI, automation, and system integrations to build intelligent workflows tailored to each organization's operational requirements.
"""
# =====================================================
# REVENUE OPERATIONS (REVOPS) CONSULTING
# =====================================================

REVOPS_KEYWORDS = [

    "revops",
    "revenue operations",
    "revenue operation",
    "revenue operations consulting",
    "revops consulting",
    "sales operations",
    "marketing operations",
    "sales ops",
    "marketing ops",
    "go to market operations",
    "gtm operations",
    "revenue optimization",
    "revenue growth",
    "pipeline management",
    "pipeline optimization",
    "sales process",
    "sales process optimization",
    "sales workflow",
    "sales efficiency",
    "revenue strategy",
    "commercial operations",
    "sales performance",
    "sales enablement",
    "revenue enablement",
    "business operations",
    "business optimization",
    "revenue consulting",
    "sales consulting",
    "business consulting",
    "growth consulting",
    "what is revops",
    "what is revenue operations",
    "tell me about revops",
    "explain revops",
    "do you provide revops consulting"

]


REVOPS_RESPONSE = """
VisionScaleX provides Revenue Operations (RevOps) Consulting to align sales, marketing, and customer success teams under a unified revenue strategy.

Our RevOps Consulting capabilities include:

• Go-To-Market (GTM) Strategy

• Sales Process Optimization

• Pipeline Management

• CRM Strategy & Optimization

• Workflow Automation

• Revenue Intelligence

• Sales Performance Analytics

• Forecasting & Reporting

• Process Standardization

• AI-Powered Revenue Optimization

Our RevOps approach helps organizations:

• Increase operational efficiency

• Improve pipeline visibility

• Accelerate revenue growth

• Reduce process bottlenecks

• Enhance cross-functional collaboration

• Build predictable and scalable revenue systems

VisionScaleX combines AI, commercial intelligence, automation, and strategic consulting to help businesses create efficient, data-driven revenue operations.
"""
# =====================================================
# EXECUTIVE OUTREACH
# =====================================================

EXECUTIVE_OUTREACH_KEYWORDS = [

    "executive outreach",
    "executive engagement",
    "executive communication",
    "executive prospecting",
    "executive targeting",
    "executive networking",
    "leadership outreach",
    "c level outreach",
    "c-suite outreach",
    "ceo outreach",
    "cto outreach",
    "cio outreach",
    "cfo outreach",
    "coo outreach",
    "founder outreach",
    "decision maker outreach",
    "decision maker engagement",
    "executive meetings",
    "executive connections",
    "executive relationship building",
    "executive sales outreach",
    "enterprise outreach",
    "enterprise prospecting",
    "high value prospecting",
    "personalized executive outreach",
    "outbound outreach",
    "b2b outreach",
    "executive contact",
    "executive lead generation",
    "executive pipeline",
    "what is executive outreach",
    "tell me about executive outreach",
    "explain executive outreach",
    "do you provide executive outreach"

]


EXECUTIVE_OUTREACH_RESPONSE = """
VisionScaleX provides AI-powered Executive Outreach services to help organizations engage senior decision-makers and accelerate enterprise sales opportunities.

Our Executive Outreach capabilities include:

• Executive & Decision-Maker Identification

• Personalized Multi-Channel Outreach

• AI-Powered Message Personalization

• Email & LinkedIn Outreach Campaigns

• Executive Relationship Building

• Strategic Account Engagement

• Follow-up Sequence Automation

• Meeting Scheduling Support

• Response Tracking & Analytics

• Enterprise Pipeline Development

Our Executive Outreach approach helps organizations:

• Reach key decision-makers faster

• Increase executive response rates

• Build meaningful business relationships

• Improve enterprise sales opportunities

• Generate high-quality meetings

• Accelerate revenue growth

VisionScaleX combines AI, commercial intelligence, automation, and personalization to deliver highly targeted executive engagement campaigns.
"""
# =====================================================
# ACCOUNT-BASED MARKETING (ABM)
# =====================================================

ABM_KEYWORDS = [

    "abm",
    "account based marketing",
    "account-based marketing",
    "account based marketing strategy",
    "account targeting",
    "target account",
    "target account marketing",
    "strategic account marketing",
    "enterprise marketing",
    "enterprise sales",
    "named account strategy",
    "key account marketing",
    "key account strategy",
    "account engagement",
    "account personalization",
    "personalized marketing",
    "b2b marketing",
    "b2b demand generation",
    "high value accounts",
    "ideal target accounts",
    "enterprise outreach",
    "enterprise campaigns",
    "decision maker targeting",
    "multi channel marketing",
    "marketing personalization",
    "sales and marketing alignment",
    "go to market strategy",
    "gtm strategy",
    "what is abm",
    "what is account based marketing",
    "tell me about abm",
    "explain account based marketing",
    "do you provide abm"

]


ABM_RESPONSE = """
VisionScaleX provides AI-powered Account-Based Marketing (ABM) solutions designed to help organizations engage high-value target accounts with personalized, data-driven campaigns.

Our ABM capabilities include:

• Ideal Customer Profile (ICP) Development

• Target Account Identification

• AI-Powered Account Research

• Buying Signal Intelligence

• Executive & Decision-Maker Mapping

• Personalized Multi-Channel Outreach

• Account Prioritization

• Strategic Account Engagement

• Sales & Marketing Alignment

• Campaign Performance Analytics

Our Account-Based Marketing approach helps organizations:

• Focus on high-value target accounts

• Improve engagement with key decision-makers

• Increase conversion rates

• Shorten enterprise sales cycles

• Maximize marketing ROI

• Build predictable revenue pipelines

VisionScaleX combines AI, commercial intelligence, automation, and personalization to deliver scalable, high-performing Account-Based Marketing strategies.
"""
STATIC_KNOWLEDGE = [

    (GREETING_KEYWORDS, GREETING_RESPONSE),

    (ABOUT_KEYWORDS, ABOUT_RESPONSE),

    (MISSION_KEYWORDS, MISSION_RESPONSE),

    (USP_KEYWORDS, USP_RESPONSE),

    (FRAMEWORK_KEYWORDS, FRAMEWORK_RESPONSE),

    (SERVICE_KEYWORDS, SERVICE_RESPONSE),

    (AI_SDR_KEYWORDS, AI_SDR_RESPONSE),

    (REVENUE_INTELLIGENCE_KEYWORDS, REVENUE_INTELLIGENCE_RESPONSE),

    (BUYING_SIGNAL_KEYWORDS, BUYING_SIGNAL_RESPONSE),

    (COLD_EMAIL_KEYWORDS, COLD_EMAIL_RESPONSE),

    (ACCOUNT_RESEARCH_KEYWORDS, ACCOUNT_RESEARCH_RESPONSE),

    (ACCOUNT_ENRICHMENT_KEYWORDS, ACCOUNT_ENRICHMENT_RESPONSE),

    (ICP_KEYWORDS, ICP_RESPONSE),

    (OWNERSHIP_MAPPING_KEYWORDS, OWNERSHIP_MAPPING_RESPONSE),

    (WORKFLOW_AUTOMATION_KEYWORDS, WORKFLOW_AUTOMATION_RESPONSE),

    (REVOPS_KEYWORDS, REVOPS_RESPONSE),

    (EXECUTIVE_OUTREACH_KEYWORDS, EXECUTIVE_OUTREACH_RESPONSE),

    (ABM_KEYWORDS, ABM_RESPONSE),

    (INDUSTRY_KEYWORDS, INDUSTRY_RESPONSE),

    (TECHNOLOGY_KEYWORDS, TECHNOLOGY_RESPONSE),

    (PRICING_KEYWORDS, PRICING_RESPONSE),

    (DEMO_KEYWORDS, DEMO_RESPONSE),

    (CONTACT_KEYWORDS, CONTACT_RESPONSE),

]

def get_static_response(query):
    query= query.strip().lower()
    for keywords, response in STATIC_KNOWLEDGE:

        if any(keyword in query for keyword in keywords):

            return response

    return None