<?php

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.
// Returns the public 'ps_checkout.command.handler.order.matrice.update_order_matrice' shared service.

return $this->services['ps_checkout.command.handler.order.matrice.update_order_matrice'] = new \PrestaShop\Module\PrestashopCheckout\Order\Matrice\CommandHandler\UpdateOrderMatriceCommandHandler(${($_ = isset($this->services['ps_checkout.event.dispatcher']) ? $this->services['ps_checkout.event.dispatcher'] : $this->load('getPsCheckout_Event_DispatcherService.php')) && false ?: '_'});
