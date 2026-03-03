import os
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

def setup_telemetry(app, engine):
    # Resource identifies the service
    resource = Resource(attributes={
        "service.name": os.getenv("OTEL_SERVICE_NAME", "hr-pulse-backend"),
        "service.version": "0.1.0"
    })

    # Tracer provider
    provider = TracerProvider(resource=resource)
    
    # OTLP Exporter to Jaeger
    otlp_endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://jaeger:4317")
    exporter = OTLPSpanExporter(endpoint=otlp_endpoint, insecure=True)
    
    # Span processor
    span_processor = BatchSpanProcessor(exporter)
    provider.add_span_processor(span_processor)
    
    # Set global tracer
    trace.set_tracer_provider(provider)

    # Instrument FastAPI
    FastAPIInstrumentor.instrument_app(app)

    # Instrument SQLAlchemy
    SQLAlchemyInstrumentor().instrument(engine=engine)

    # Instrument Requests (used by Azure SDK and others)
    RequestsInstrumentor().instrument()

    return provider
