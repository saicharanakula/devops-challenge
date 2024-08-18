def before_all(context):
    # Set default base URL
    context.base_url = "http://localhost"

def before_feature(context, feature):
    if 'base_url' in context.config.userdata:
        context.base_url = context.config.userdata['base_url']
