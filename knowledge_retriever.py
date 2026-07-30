from vsx_knowledge import VSX_KNOWLEDGE


def get_relevant_knowledge(user_message):

    message = user_message.lower()

    if any(word in message for word in [
        "hi",
        "hello",
        "hey",
        "hii",
        "good morning",
        "good afternoon",
        "good evening"
    ]):

        return """
        You are VisionScaleX AI Assistant.

        Respond warmly:

        Hi! 👋 Welcome to VisionScaleX.

        I can help you with information about our services, solutions, pricing, industries, framework, and contact details.

        How can I assist you today?
        """
    elif any(word in message for word in [
            "pricing",
            "price",
            "cost",
            "plans",
            "package",
            "packages",
            "fee",
            "fees",
            "charge",
            "charges",
            "how much",
            "how much does"
    ]):
        return """
              VisionScaleX provides customized pricing based on business requirements.
        
              Pricing depends on:
            • GTM requirements
            • Target market size
            • Automation needs
            • Outreach volume
        
              For detailed pricing:
        
              Sales Email:
              sales@visionscalex.com
        
              Website:
             www.visionscalex.com
             """

    elif any(word in message for word in [
        "mission",
        "philosophy",
        "goal"
    ]):
        return VSX_KNOWLEDGE["mission"]


    elif any(word in message for word in [
        "framework",
    "frameworks",
    "select",
    "sense",
    "strike",
    "vsx framework",
    "visionscalex framework",
    "your framework",
    "company framework",
    "working framework",
    "sales framework",
    "ai framework",
    "go to market framework",
    "gtm framework",
    "methodology",
    "process",
    "workflow",
    "approach",
    "strategy",
    "how do you work",
    "how you work",
    "how does visionscalex work",
    "how does your company work",
    "how does your framework work",
    "your process",
    "your methodology",
    "your approach",
    "working model",
    "business model",
    "operating model",
    "execution model",
    "engagement model",
    "implementation process",
    "implementation methodology",
    "delivery process",
    "delivery model",
    "sales process",
    "lead generation process",
    "customer acquisition process"
    ]):
        return VSX_KNOWLEDGE["framework"]


    elif any(word in message for word in [
        "service",
        "solution",
        "offer",
        "provide"
    ]):
        return VSX_KNOWLEDGE["services"]


    elif any(word in message for word in [
        "industry",
        "sector",
        "client"
    ]):
        return VSX_KNOWLEDGE["industries"]


    elif any(word in message for word in [
        "technology",
        "ai",
        "human"
    ]):
        return VSX_KNOWLEDGE["technology"]


    elif any(word in message for word in [
        "advantage",
        "different",
        "why"
    ]):
        return VSX_KNOWLEDGE["advantages"]


    elif any(word in message for word in [
        "result",
        "case study",
        "success",
        "case studies",
        "proof",
        "relevant work",
        "relevant proof",
    ]):
        return VSX_KNOWLEDGE["results"]


    elif any(word in message for word in [
        "contact",
        "email",
        "phone",
        "address",
        "headquarter",
        "headquarters",
        "website",
        "connect"
    ]):
        return VSX_KNOWLEDGE["contact"]

    if any(word in message for word in [
            "about",
            "vision scalex",
            "visionscalex",
            "company",
            "about visionscalex",
            "what is visionscalex",
            "who are you",
            "tell me about the company",
            "company overview",
            "about you"
        ]):
            return VSX_KNOWLEDGE["about"]


    return ""