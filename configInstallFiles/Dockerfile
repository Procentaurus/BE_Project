FROM prestashop/prestashop:1.7.8-apache

COPY ssl.crt /etc/ssl/certs/ssl.crt
COPY ssl.crt /usr/local/share/ca-certificates/ssl.crt
COPY ssl.key /etc/ssl/private/ssl.key
COPY prestashop-ssl.conf /etc/apache2/sites-available/prestashop-ssl.conf

RUN update-ca-certificates && a2enmod ssl && a2ensite prestashop-ssl