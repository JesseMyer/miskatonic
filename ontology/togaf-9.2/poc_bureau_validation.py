"""
Miskatonic Phase 2 PoC — Bureau Ontology Validation
Requires: pip install rdflib
Usage: python3 poc_bureau_validation.py
"""
from rdflib import Graph, Namespace, RDF, OWL, RDFS

g = Graph()
g.parse("OntologyTOGAFContentMetamodelV2-Miskatonic.ttl", format="turtle")

TOGAF = Namespace("http://www.semanticweb.org/ontologies/2020/4/OntologyTOGAFContentMetamodel.owl#")
MSK   = Namespace("https://github.com/JesseMyer/miskatonic/ontology/togaf-9.2/governance#")


def validate_construct_relationship(domain_label, range_label):
    """
    Given two construct names, returns all legal named relationships
    between them per TOGAF 9.2 Figure 30-7.
    Returns empty list if no legal relationship exists — Bureau finding candidate.
    """
    q = f"""
    PREFIX togaf: <http://www.semanticweb.org/ontologies/2020/4/OntologyTOGAFContentMetamodel.owl#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?rel_label WHERE {{
        ?rel a owl:ObjectProperty ;
             rdfs:label ?rel_label ;
             rdfs:domain ?domain ;
             rdfs:range  ?range .
        ?domain rdfs:label "{domain_label}" .
        ?range  rdfs:label "{range_label}" .
    }}
    """
    return [str(row.rel_label) for row in g.query(q)]


def get_bureau_finding_triggers():
    """Returns all constructs with Bureau finding triggers annotated in the ontology."""
    q = """
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX msk: <https://github.com/JesseMyer/miskatonic/ontology/togaf-9.2/governance#>
    SELECT ?label ?note WHERE {
        ?c a owl:Class ;
           rdfs:label ?label ;
           msk:miskatonicNote ?note .
        FILTER(CONTAINS(STR(?note), "Bureau finding"))
    }
    """
    return [(str(r.label), str(r.note)) for r in g.query(q)]


def get_all_legal_relationships_from(construct_label):
    """Returns all constructs this construct can legally relate to per Figure 30-7."""
    q = f"""
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?rel_label ?range_label WHERE {{
        ?rel a owl:ObjectProperty ;
             rdfs:label ?rel_label ;
             rdfs:domain ?domain ;
             rdfs:range  ?range .
        ?domain rdfs:label "{construct_label}" .
        ?range  rdfs:label ?range_label .
    }}
    """
    return [(str(r.rel_label), str(r.range_label)) for r in g.query(q)]


if __name__ == "__main__":
    print("=== Miskatonic Bureau Ontology Validation PoC ===")
    print()

    # Test 1: BusinessCapability -> ValueStream (should be legal)
    result = validate_construct_relationship("Business Capability", "Value Stream")
    print(f"BusinessCapability -> ValueStream: {result if result else 'NO LEGAL RELATIONSHIP — Bureau finding'}")

    # Test 2: WorkPackage -> Capability (should be legal)
    result = validate_construct_relationship("Work Package", "Capability")
    print(f"WorkPackage -> Capability: {result if result else 'NO LEGAL RELATIONSHIP — Bureau finding'}")

    # Test 3: Capability -> Driver (should be ILLEGAL)
    result = validate_construct_relationship("Capability", "Driver")
    print(f"Capability -> Driver: {result if result else 'NO LEGAL RELATIONSHIP — Bureau finding'}")

    print()
    print("Bureau finding triggers:")
    for label, note in get_bureau_finding_triggers():
        print(f"  [{label}]: {note[:80]}...")

    print()
    print("Legal relationships from OrganizationUnit:")
    for rel, target in get_all_legal_relationships_from("Organization Unit"):
        print(f"  OrganizationUnit --[{rel}]--> {target}")
