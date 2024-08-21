# Nginx
k8s_yaml('nginx/k8s/nginx.yaml')
k8s_resource(objects=['nginx-config:ConfigMap:default'], new_name='nginx-config', labels='Nginx')
k8s_resource('nginx-deployment', resource_deps=['nginx-config'], labels='Nginx')

# UI
# check if UI repo has been checked out
USE_UI = os.path.exists('./ui/k8s')
if USE_UI:
    docker_build(
        'architect-design-poc-ui',
        context='ui',
        dockerfile='./ui/Dockerfile',
        build_args={'node_env': 'development'},
        entrypoint='npm run dev',
        only=['src', 'webpack.config.js', 'package.json', 'package-lock.json'],
        live_update=[
            sync('ui/src', '/usr/app/src'),
        ]
    )

    k8s_yaml('ui/k8s/ui.yaml')
    k8s_resource('ui-deployment', new_name='ui', labels='Frontend')

# GraphQL
# check if graphql repo checked out
USE_GRAPHQL = os.path.exists('./graphql-api/k8s')
if USE_GRAPHQL:
    docker_build(
        'us-west2-docker.pkg.dev/fir-architect-test-out/architect-try-gar/firebase-graphql-docker-k8s-test-out',
        context='graphql-api',
        dockerfile='./graphql-api/Dockerfile',
        build_args={'node_env': 'development'},
        entrypoint='npx nodemon index.js',
        only=['index.js', 'package.json', 'package-lock.json', 'middlewares', 'secrets'],
        live_update=[
            sync('graphql-api/index.js', '/usr/app/index.js'),
        ]
    )
    k8s_yaml('graphql-api/k8s/graphql.yaml')
    k8s_resource('graphql-deployment', new_name='graphql', labels='Backend',port_forwards='30080:3000')

# PostgREST API
k8s_yaml('postgresql-db/k8s/postgrest.yaml')
k8s_yaml('postgresql-db/k8s/postgres-local-config.yaml')
k8s_resource(objects=['postgres-config:ConfigMap:default'], new_name='postgres-config', labels='DB')
k8s_resource('postgrest-deployment', new_name='postgrest-api', resource_deps=['postgres-config'], labels='DB')

# PostgreSQL DB
k8s_yaml('postgresql-db/k8s/postgresql.yaml')
k8s_resource('postgresql-deployment', new_name='postgresql-db', labels='DB' )
k8s_yaml('postgresql-db/k8s/sqlalchemy.yaml')
docker_build(
    'us-west2-docker.pkg.dev/fir-architect-test-out/architect-try-gar/sqlalchemy-migration-seed',
    context='postgresql-db/app',
    dockerfile='./postgresql-db/app/Dockerfile'
)
k8s_resource('sqlalchemy-migration-job', new_name='sqlalchemy', labels='DB', resource_deps=['postgresql-db', 'postgres-config'])

