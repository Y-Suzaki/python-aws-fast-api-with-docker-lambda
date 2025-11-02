FROM public.ecr.aws/docker/library/python:3.12-slim

# Copy Lambda Web Adapter.
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.9.1 /lambda-adapter /opt/extensions/lambda-adapter
WORKDIR /var/task

# Set application port.
ENV PORT=8000

# Install libralies and copy source codes.
COPY ./src/ ./
RUN python -m pip install -r requirements.txt


# Run application via uvicorn.
CMD ["sh", "-c", "exec uvicorn --port=$PORT main:app"]
