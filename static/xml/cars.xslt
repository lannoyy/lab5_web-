<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version = "1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html>
    <head>
        <title>Buildings</title>
    </head>
    <body>
        <table border = "1">
    <tbody>
    <xsl:for-each select="cars/car">
        <tr>
            <th>
        <xsl:value-of select="@id"/>
            </th>
        <th>
        <xsl:value-of select="brand"/>
            </th>
        <th>
            <xsl:value-of select="year"/>
            </th>
        <th>
            <xsl:value-of select="horsepower"/>
            </th>
        </tr>
        </xsl:for-each>
        </tbody>
        </table>
        </body>
    </html>
</xsl:template></xsl:stylesheet>