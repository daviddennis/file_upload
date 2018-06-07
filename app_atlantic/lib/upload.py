from datetime import datetime
import csv
import pytz

from app_atlantic.constants import EXCLUDED_FIELD_TYPES
from app_atlantic.models import Customer, Product, Upload


def process_file_upload(filename, fh):
    new_upload = Upload.objects.create(filename=filename)
    for line in fh:
        line = line.decode('utf-8')
        for row in csv.reader([line], delimiter="\t"):
            if len(row) != 11:
                # TODO: log exception
                continue

            data = {}
            i = 0
            for _model in [Customer, Product]:
                model_name = _model.__name__
                for field in _model._meta.get_fields():
                    field_type = field.get_internal_type()
                    if field_type not in EXCLUDED_FIELD_TYPES:
                        val = row[i]
                        if field_type == 'DateTimeField':
                            dt = datetime.strptime(val, '%Y-%m-%dT%H:%MZ')
                            dt = dt.replace(tzinfo=pytz.UTC)
                            data[field.name] = dt
                        else:
                            data[field.name] = val
                        i += 1

                data['upload'] = new_upload
                _model.objects.create(**data)

                data = {}