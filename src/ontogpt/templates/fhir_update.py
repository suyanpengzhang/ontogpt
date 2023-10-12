from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel as BaseModel, Field
import sys
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


metamodel_version = "None"
version = "None"

class ConfiguredBaseModel(BaseModel,
                validate_assignment = True,
                validate_default = True,
                extra = 'forbid',
                arbitrary_types_allowed = True,
                use_enum_values = True):
    pass


class NullDataOptions(str, Enum):
    
    
    UNSPECIFIED_METHOD_OF_ADMINISTRATION = "UNSPECIFIED_METHOD_OF_ADMINISTRATION"
    
    NOT_APPLICABLE = "NOT_APPLICABLE"
    
    NOT_MENTIONED = "NOT_MENTIONED"
    
    

class Bundle(ConfiguredBaseModel):
    
    patient: Optional[str] = Field(None, description="""patient information""")
    observation: Optional[str] = Field(None, description="""results for interviews (e.g., cognitive tests) and imaging (e.g., PET, MRI)""")
    medicationstatement: Optional[str] = Field(None, description="""information of the medications""")
    condition: Optional[str] = Field(None, description="""information of the diagnosis""")
    organization: Optional[str] = Field(None, description="""information of the site""")
    encounter: Optional[str] = Field(None, description="""information of the visit""")
    

class ExtractionResult(ConfiguredBaseModel):
    """
    A result of extracting knowledge on text
    """
    input_id: Optional[str] = Field(None)
    input_title: Optional[str] = Field(None)
    input_text: Optional[str] = Field(None)
    raw_completion_output: Optional[str] = Field(None)
    prompt: Optional[str] = Field(None)
    extracted_object: Optional[Any] = Field(None, description="""The complex objects extracted from the text""")
    named_entities: Optional[List[Any]] = Field(default_factory=list, description="""Named entities extracted from the text""")
    

class NamedEntity(ConfiguredBaseModel):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    

class Patient(NamedEntity):
    
    identifier: Optional[str] = Field(None)
    gender: Optional[str] = Field(None)
    birthdate: Optional[str] = Field(None)
    maritalstatus: Optional[str] = Field(None)
    latino: Optional[str] = Field(None)
    ethnicity: Optional[str] = Field(None)
    education: Optional[str] = Field(None)
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    

class Observation(NamedEntity):
    
    fdg: Optional[str] = Field(None, description="""glucose analogue""")
    av45: Optional[str] = Field(None, description="""florbetapir""")
    pib: Optional[str] = Field(None, description="""Pittsburgh compound B""")
    entorhinal: Optional[str] = Field(None, description="""entorhinal cortex""")
    fbb: Optional[str] = Field(None, description="""blood-brain barrier""")
    fusiform: Optional[str] = Field(None, description="""fusiform gyrus""")
    hippocampus: Optional[str] = Field(None, description="""hippocampus""")
    icv: Optional[str] = Field(None, description="""Intracranial volume""")
    midtemp: Optional[str] = Field(None, description="""middle temporal gyrus""")
    ventricles: Optional[str] = Field(None, description="""Ventricular volume""")
    wholebrain: Optional[str] = Field(None, description="""whole brain volume""")
    abeta: Optional[str] = Field(None, description="""amyloid beta""")
    apoe4: Optional[str] = Field(None, description="""apolipoprotein E4""")
    effective: Optional[str] = Field(None, description="""exam date""")
    ptau: Optional[str] = Field(None, description="""Phospho-Tau (p-Tau)""")
    tau: Optional[str] = Field(None, description="""tau""")
    adas11: Optional[str] = Field(None, description="""Alzheimer’s Disease Assessment Scale (11 questions)""")
    adas13: Optional[str] = Field(None, description="""Alzheimer’s Disease Assessment Scale (13 questions)""")
    adasq4: Optional[str] = Field(None, description="""Alzheimer’s Disease Assessment Scale (non-cognitive tests)""")
    cdrsb: Optional[str] = Field(None, description="""clinical dementia rating scale–sum of boxes""")
    digitscor: Optional[str] = Field(None, description="""digit span test score""")
    ecogptdivatt: Optional[str] = Field(None, description="""Everyday Cognition (ECog)  patient reported version (ECogPT), divided attention""")
    ecogptlang: Optional[str] = Field(None, description="""Everyday Cognition (ECog)  patient reported version (ECogPT), langague""")
    ecogptmem: Optional[str] = Field(None, description="""Everyday Cognition (ECog)  patient reported version (ECogPT), memory""")
    ecogptorgan: Optional[str] = Field(None, description="""Everyday Cognition (ECog)  patient reported version (ECogPT), organizational""")
    ecogptplan: Optional[str] = Field(None, description="""Everyday Cognition (ECog)  patient reported version (ECogPT), planning""")
    ecogpttotal: Optional[str] = Field(None, description="""Everyday Cognition (ECog)  patient reported version (ECogPT), tottal""")
    ecogptvisspat: Optional[str] = Field(None, description="""Everyday Cognition (ECog)  patient reported version (ECogPT), visual-spatial""")
    ecogspdivatt: Optional[str] = Field(None, description="""Everyday Cognition (ECog) the study partner reported version (ECogSP), divided attention""")
    ecogsplang: Optional[str] = Field(None, description="""Everyday Cognition (ECog) the study partner reported version (ECogSP), langague""")
    ecogspmem: Optional[str] = Field(None, description="""Everyday Cognition (ECog) the study partner reported version (ECogSP), memory""")
    ecogsporgan: Optional[str] = Field(None, description="""Everyday Cognition (ECog) the study partner reported version (ECogSP), organizational""")
    ecogspplan: Optional[str] = Field(None, description="""Everyday Cognition (ECog) the study partner reported version (ECogSP), planning""")
    ecogsptotal: Optional[str] = Field(None, description="""Everyday Cognition (ECog) the study partner reported version (ECogSP), tottal""")
    ecogspvisspat: Optional[str] = Field(None, description="""Everyday Cognition (ECog) the study partner reported version (ECogSP), visual-spatial""")
    faq: Optional[str] = Field(None, description="""The Functional Activities Questionnaire (FAQ)""")
    ldeltotal: Optional[str] = Field(None, description="""Logical Memory (LM), delayed recall""")
    mmse: Optional[str] = Field(None, description="""A Mini-Mental State Examination (11 questions)""")
    moca: Optional[str] = Field(None, description="""The Montreal Cognitive Assessment (MoCA) test can detect mild cognitive impairment or early signs of dementia.""")
    mpaccdigit: Optional[str] = Field(None, description="""the Modified Preclinical Alzheimer Cognitive Composite with Digit test (mPACCdigit)""")
    mpacctrailsb: Optional[str] = Field(None, description="""Modified Preclinical Alzheimer Cognitive Composite with Trails test (mPACCtrailsB)""")
    ravlt_forgetting: Optional[str] = Field(None, description="""from Rey Auditory Verbal Learning Test (RAVLT), forgetting""")
    ravlt_immediate: Optional[str] = Field(None, description="""from Rey Auditory Verbal Learning Test (RAVLT), immediate recall trials""")
    ravlt_learning: Optional[str] = Field(None, description="""from Rey Auditory Verbal Learning Test (RAVLT)""")
    ravlt_perc_forgetting: Optional[str] = Field(None, description="""from Rey Auditory Verbal Learning Test (RAVLT)""")
    trabscor: Optional[str] = Field(None, description="""Trail Making Test A-B (TMT A-B) TMT A-B encompasses two trials, A and B""")
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    

class MedicationStatement(NamedEntity):
    
    medication: Optional[str] = Field(None)
    reason: Optional[str] = Field(None)
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    

class Condition(NamedEntity):
    
    code: Optional[str] = Field(None, description="""diagnosis or comorbidities""")
    evidence: Optional[str] = Field(None, description="""symptoms""")
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    

class Organization(NamedEntity):
    
    name: Optional[str] = Field(None)
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    

class Encounter(NamedEntity):
    
    plannedstartdate: Optional[str] = Field(None, description="""month of data""")
    appointment: Optional[str] = Field(None, description="""visit code""")
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    

class CompoundExpression(ConfiguredBaseModel):
    
    None
    

class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    subject: Optional[str] = Field(None)
    predicate: Optional[str] = Field(None)
    object: Optional[str] = Field(None)
    qualifier: Optional[str] = Field(None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""")
    subject_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the subject of the statement, e.g. \"high dose\" or \"intravenously administered\"""")
    object_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the object of the statement, e.g. \"severe\" or \"with additional complications\"""")
    

class TextWithTriples(ConfiguredBaseModel):
    
    publication: Optional[Publication] = Field(None)
    triples: Optional[List[Triple]] = Field(default_factory=list)
    

class RelationshipType(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    

class Publication(ConfiguredBaseModel):
    
    id: Optional[str] = Field(None, description="""The publication identifier""")
    title: Optional[str] = Field(None, description="""The title of the publication""")
    abstract: Optional[str] = Field(None, description="""The abstract of the publication""")
    combined_text: Optional[str] = Field(None)
    full_text: Optional[str] = Field(None, description="""The full text of the publication""")
    

class AnnotatorResult(ConfiguredBaseModel):
    
    subject_text: Optional[str] = Field(None)
    object_id: Optional[str] = Field(None)
    object_text: Optional[str] = Field(None)
    


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Bundle.model_rebuild()
ExtractionResult.model_rebuild()
NamedEntity.model_rebuild()
Patient.model_rebuild()
Observation.model_rebuild()
MedicationStatement.model_rebuild()
Condition.model_rebuild()
Organization.model_rebuild()
Encounter.model_rebuild()
CompoundExpression.model_rebuild()
Triple.model_rebuild()
TextWithTriples.model_rebuild()
RelationshipType.model_rebuild()
Publication.model_rebuild()
AnnotatorResult.model_rebuild()
    
