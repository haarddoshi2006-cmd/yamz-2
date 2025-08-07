#!/usr/bin/env python3

from app import create_app, db
from app.term.models import Term

def check_database():
    app = create_app()
    with app.app_context():
        # Check specific terms
        white_ice = Term.query.filter_by(term_string='White ice').first()
        young_ice = Term.query.filter_by(term_string='Young ice').first()
        
        print(f"White ice exists: {white_ice is not None}")
        print(f"Young ice exists: {young_ice is not None}")
        print(f"Total terms in database: {Term.query.count()}")
        
        print("\nFirst 10 terms:")
        for term in Term.query.limit(10).all():
            print(f"- {term.term_string} (ID: {term.id}, Status: {term.status})")
        
        # Check for any terms containing 'ice'
        ice_terms = Term.query.filter(Term.term_string.ilike('%ice%')).all()
        print(f"\nTerms containing 'ice': {len(ice_terms)}")
        for term in ice_terms:
            print(f"- {term.term_string}")

if __name__ == "__main__":
    check_database()
