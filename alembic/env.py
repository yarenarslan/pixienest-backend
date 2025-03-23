from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.core.config import settings  # Veritabanı bağlantısını settings'ten alacağız.
from app.models import Base

# Alembic config nesnesini al
config = context.config

# ENV dosyasındaki DATABASE_URL değişkenini Alembic'e aktar
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# Log yapılandırması
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Veritabanı modellerini buraya ekleyebilirsin
from app.models import Base  # Model dosyanı içe aktar
target_metadata = Base.metadata  # Alembic için kullanılacak metadata

def run_migrations_offline() -> None:
    """Offline migration çalıştırır."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Online migration çalıştırır."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
