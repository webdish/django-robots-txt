from django.views.generic import TemplateView


class RobotsTextView(TemplateView):
    """
    A simple view with mimetype text/plain
    """
    template_name = 'robots.txt'

    def render_to_response(self, context, **kwargs):
        return super(TextView, self).render_to_response(
            context,
            content_type='text/plain',
            **kwargs
        )