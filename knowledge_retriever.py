from vsx_knowledge import VSX_KNOWLEDGE


def get_relevant_knowledge(user_message):

    message = user_message.lower()

    if any(word in message for word in [
        "about",
        "vision scalex",
        "visionscalex",
        "company",
        "who are you"
    ]):
        return VSX_KNOWLEDGE["about"]


    elif any(word in message for word in [
        "mission",
        "philosophy",
        "goal"
    ]):
        return VSX_KNOWLEDGE["mission"]


    elif any(word in message for word in [
        "framework",
        "select",
        "sense",
        "strike"
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
        "success"
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

    elif any(word in message for word in [
        "price",
        "pricing",
        "cost",
        "plan",
        "package"
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


    return ""