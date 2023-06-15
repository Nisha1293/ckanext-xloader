import ckan.plugins.toolkit as toolkit


def xloader_status(resource_id):
    try:
        return toolkit.get_action('xloader_status')(
            {}, {'resource_id': resource_id})
    except toolkit.ObjectNotFound:
        return {
            'status': 'unknown'
        }


def xloader_status_description(status):
    _ = toolkit._

    if status.get('status'):
        captions = {
            'complete': _('Complete'),
            'pending': _('Pending'),
            'submitting': _('Submitting'),
            'error': _('Error'),
        }

        return captions.get(status['status'], status['status'].capitalize())
    else:
        return _('Not Uploaded Yet')


def is_xloader_format(resource_format):
    from ckanext.xloader.plugin import XLoaderFormats

    return XLoaderFormats.is_it_an_xloader_format(resource_format)


def is_xloader_type(resource_url_type):
    try:
        return resource_url_type not in toolkit.h.datastore_rw_resource_url_types()
    except AttributeError:
        return (resource_url_type == 'upload' or resource_url_type == '')
