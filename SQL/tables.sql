-- ****************** SqlDBM: Microsoft SQL Server ******************
-- ******************************************************************

-- ************************************** [dbo].[VENDEDOR]
CREATE TABLE [dbo].[VENDEDOR]
(
    [IdVendedor] int         IDENTITY(1,1),
    [Nombre]     varchar(50) NOT NULL,
    [Apellido]   varchar(50) NOT NULL,


    CONSTRAINT [PK_persona] PRIMARY KEY CLUSTERED ([IdVendedor] ASC)
);
GO
-- ************************************** [dbo].[Tipo]
CREATE TABLE [dbo].[Tipo]
(
    [IdTipo] int IDENTITY(1,1),
    [Tipo]   varchar(50) NOT NULL,


    CONSTRAINT [PK_tipo] PRIMARY KEY CLUSTERED ([IdTipo] ASC)
);
GO
-- ************************************** [dbo].[PAGINA]
CREATE TABLE [dbo].[PAGINA]
(
    [IdPagina]  int          IDENTITY(1,1),
    [Nombre]    varchar(50)  NOT NULL,
    [UrlPagina] varchar(250) NOT NULL,


    CONSTRAINT [PK_pagina] PRIMARY KEY CLUSTERED ([IdPagina] ASC)
);
GO
-- ************************************** [dbo].[CONTACTO]
CREATE TABLE [dbo].[CONTACTO]
(
    [IdContacto] int         IDENTITY(1,1),
    [Contacto]   varchar(50) NOT NULL,
    [IdTipo]     int         NOT NULL,


    CONSTRAINT [PK_contacto_clone] PRIMARY KEY CLUSTERED ([IdContacto] ASC),
    CONSTRAINT [FK_59] FOREIGN KEY ([IdTipo]) REFERENCES [dbo].[Tipo] ([IdTipo])
);
GO


CREATE NONCLUSTERED INDEX [fkIdx_60] ON [dbo].[CONTACTO]
    (
     [IdTipo] ASC
        )

GO
-- ************************************** [dbo].[AUTO]
CREATE TABLE [dbo].[AUTO]
(
    [IdAuto]       int          IDENTITY(1,1),
    [IdVendedor]   int          NOT NULL,
    [Anno]         varchar(4)   NOT NULL,
    [Kilometros]   int          NOT NULL,
    [Tipo]         varchar(50)  NOT NULL,
    [Transmision]  varchar(50)  NOT NULL,
    [Combustible]  varchar(50)  NOT NULL,
    [Localizacion] varchar(200) NOT NULL,
    [Marca]        varchar(50)  NOT NULL,
    [Modelo]       varchar(50)  NOT NULL,
    [Precio]       float        NOT NULL,
    [Motor]        varchar(50)  NOT NULL,
    [Estilo]       varchar(50)  NOT NULL,
    [Asientos]     int          NOT NULL,
    [Chasis]       varchar(50)  NOT NULL,


    CONSTRAINT [PK_autos] PRIMARY KEY CLUSTERED ([IdAuto] ASC),
    CONSTRAINT [FK_29] FOREIGN KEY ([IdVendedor]) REFERENCES [dbo].[VENDEDOR] ([IdVendedor])
);
GO


CREATE NONCLUSTERED INDEX [fkIdx_30] ON [dbo].[AUTO]
    (
     [IdVendedor] ASC
        )

GO
-- ************************************** [dbo].[PUBLICACION]
CREATE TABLE [dbo].[PUBLICACION]
(
    [IdPublicacion]    int          IDENTITY(1,1),
    [IdAuto]           int          NOT NULL,
    [IdPagina]         int          NOT NULL,
    [FechaPublicacion] datetime     NOT NULL,
    [FechaScraping]    datetime     NOT NULL,
    [UrlPublicacion]   varchar(250) NOT NULL,


    CONSTRAINT [PK_publicacion] PRIMARY KEY CLUSTERED ([IdPublicacion] ASC),
    CONSTRAINT [FK_65] FOREIGN KEY ([IdAuto]) REFERENCES [dbo].[AUTO] ([IdAuto]),
    CONSTRAINT [FK_75] FOREIGN KEY ([IdPagina]) REFERENCES [dbo].[PAGINA] ([IdPagina])
);
GO


CREATE NONCLUSTERED INDEX [fkIdx_66] ON [dbo].[PUBLICACION]
    (
     [IdAuto] ASC
        )

GO

CREATE NONCLUSTERED INDEX [fkIdx_76] ON [dbo].[PUBLICACION]
    (
     [IdPagina] ASC
        )

GO
-- ************************************** [dbo].[CONTACTOxVENDEDOR]
CREATE TABLE [dbo].[CONTACTOxVENDEDOR]
(
    [IdContacto]   int IDENTITY(1,1),
    [IdVendedor]   int NOT NULL,
    [IdContacto_1] int NOT NULL,


    CONSTRAINT [PK_contacto] PRIMARY KEY CLUSTERED ([IdContacto] ASC),
    CONSTRAINT [FK_43] FOREIGN KEY ([IdVendedor]) REFERENCES [dbo].[VENDEDOR] ([IdVendedor]),
    CONSTRAINT [FK_56] FOREIGN KEY ([IdContacto_1]) REFERENCES [dbo].[CONTACTO] ([IdContacto])
);
GO


CREATE NONCLUSTERED INDEX [fkIdx_44] ON [dbo].[CONTACTOxVENDEDOR]
    (
     [IdVendedor] ASC
        )

GO

CREATE NONCLUSTERED INDEX [fkIdx_57] ON [dbo].[CONTACTOxVENDEDOR]
    (
     [IdContacto_1] ASC
        )

GO
