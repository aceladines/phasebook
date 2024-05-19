from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """


    # Implement search here!
    matched_users = set()

    results = [
        obj for obj in USERS
          if (
            (args.get('id') and obj.get('id') == args['id']) or
            (args.get('name') and args['name'].lower() in obj.get('name', '').lower()) or
            (args.get('age') and int(args['age']) - 1 <= int(obj.get('age', 0)) <= int(args['age']) + 1) or
            (args.get('occupation') and args['occupation'].lower() in obj.get('occupation', '').lower())
        )

        if obj['id'] not in matched_users and not matched_users.add(obj['id'])
    ]

    results.sort(key=lambda user: (
        0 if args.get('id') and user.get('id') == args['id'] else 1,
        0 if args.get('name') and args['name'].lower() in user.get('name', '').lower() else 1,
        0 if args.get('age') and int(args['age']) - 1 <= int(user.get('age', 0)) <= int(args['age']) + 1 else 1,
        0 if args.get('occupation') and args['occupation'].lower() in user.get('occupation', '').lower() else 1
    ))

    return results


