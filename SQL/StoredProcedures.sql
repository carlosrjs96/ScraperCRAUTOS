USE [ScraperReventaAutos]
GO
/****** Object:  StoredProcedure [dbo].[insertContacto]    Script Date: 13/06/2021 16:10:23 ******/
CREATE PROCEDURE [dbo].[insertContacto] (
    @Contacto varchar(50),
    @Tipo     varchar(50)
)
AS
BEGIN
    Declare @IdContacto int;
    Declare @IdTipo int;
    Select  @IdTipo = IdTipo from Tipo where Tipo.Tipo = @Tipo
    INSERT INTO [CONTACTO]
    (
        Contacto,
        IdTipo
    )
    VALUES  (
                @Contacto,
                @IdTipo
            )
    select @IdContacto = Scope_Identity();

    SELECT	'Current_Identity' = @IdContacto;
END
go
/****** Object:  StoredProcedure [dbo].[insertContactoXVendedor]    Script Date: 13/06/2021 16:10:23 ******/
CREATE PROCEDURE [dbo].[insertContactoXVendedor](@IdVendedor int, -- int NOT NULL
                                                 @IdContacto int -- int NOT NULL
)
AS
BEGIN
    INSERT INTO [CONTACTOxVENDEDOR]
    (IdVendedor,
     IdContacto_1)
    VALUES (@IdVendedor,
            @IdContacto)

    select @IdContacto = Scope_Identity();

    SELECT 'Current_Identity' = @IdContacto;
END
go
/****** Object:  StoredProcedure [dbo].[insertDefaultData]    Script Date: 13/06/2021 16:10:23 ******/
CREATE PROCEDURE [dbo].[insertDefaultData]
AS
BEGIN
    INSERT INTO [Tipo](Tipo)  VALUES  ('TELEFONO')
    INSERT INTO [Tipo](Tipo)  VALUES  ('WHATSAPP')
    INSERT INTO [Tipo](Tipo)  VALUES  ('CORREO')
    INSERT INTO [Tipo](Tipo)  VALUES  ('SKYPE')
    INSERT INTO [Tipo](Tipo)  VALUES  ('FACEBOOK')
    INSERT INTO [PAGINA](Nombre,UrlPagina)  VALUES  ('CRAUTOS','www.crautos.com')
END
go
/****** Object:  StoredProcedure [dbo].[insertPublicacion]    Script Date: 13/06/2021 16:10:23 ******/
CREATE PROCEDURE [dbo].[insertPublicacion](@Nombre varchar(50),
                                           @Apellido varchar(50),
                                           @Anno varchar(4),
                                           @Kilometros int,
                                           @Tipo varchar(50),
                                           @Transmision varchar(50),
                                           @Combustible varchar(50),
                                           @Localizacion varchar(200),
                                           @Marca varchar(50),
                                           @Modelo varchar(50),
                                           @Precio float,
                                           @Motor varchar(50),
                                           @Estilo varchar(50),
                                           @Asientos int,
                                           @Chasis varchar(50),
                                           @NombrePagina varchar(50),
                                           @FechaPublicacion datetime,
                                           @FechaScraping datetime,
                                           @UrlPublicacion varchar(250))
AS
BEGIN
    Declare @IdVendedor int;
    INSERT INTO [VENDEDOR]
    (Nombre,
     Apellido)
    VALUES (@Nombre,
            @Apellido)
    select @IdVendedor = Scope_Identity();

    DECLARE @IdAuto int;
    INSERT INTO [AUTO]
    (IdVendedor,
     Anno,
     Kilometros,
     Tipo,
     Transmision,
     Combustible,
     Localizacion,
     Marca,
     Modelo,
     Precio,
     Motor,
     Estilo,
     Asientos,
     Chasis)
    VALUES (@IdVendedor,
            @Anno,
            @Kilometros,
            @Tipo,
            @Transmision,
            @Combustible,
            @Localizacion,
            @Marca,
            @Modelo,
            @Precio,
            @Motor,
            @Estilo,
            @Asientos,
            @Chasis)
    select @IdAuto = Scope_Identity();


    DECLARE @IdPagina int;
    Select @IdPagina = IdPagina
    from PAGINA
    where PAGINA.Nombre = @NombrePagina

    INSERT INTO [dbo].[PUBLICACION]
    (IdAuto,
     IdPagina,
     FechaPublicacion,
     FechaScraping,
     UrlPublicacion)
    VALUES (@IdAuto,
            @IdPagina,
            @FechaPublicacion,
            @FechaScraping,
            @UrlPublicacion)


    SELECT IDENT_CURRENT ('VENDEDOR') AS Current_Identity;
END
go